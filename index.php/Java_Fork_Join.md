---
title: Java Fork/Join
layout: default
permalink: /index.php/Java_Fork_Join
---

# Java Fork/Join


## Использование Fork/Join для поиска файлов

```gdscript
public class ForkJoinTest {

    @Test
    public void forkJoinSearch() {
        ForkJoinPool forkJoinPool = new ForkJoinPool();
        Stream<File> result = forkJoinPool.invoke(new DirWalker(new File("C:/"), "ubs"));
        result.forEach(System.out::println);
        System.out.println("Done");
    }

    static class DirWalker extends RecursiveTask<Stream<File>> {
        private File dir;
        private String name;

        public DirWalker(File dir, String name) {
            if (|  dir.isDirectory()) { |                throw new IllegalArgumentException("not a dir"); |            }
            this.name = name;
            this.dir = dir;
        }

        @Override
        protected Stream<File> compute() {
            // System.out.println("looking into " + dir);
            List<File> all = toList(dir.listFiles());

            List<ForkJoinTask<Stream<File>>> tasks = new LinkedList<>();
            tasks.add(new FileLooker(all.stream(), name).fork());

            Stream<File> dirs = all.stream().filter(f -> f.isDirectory());
            Stream<ForkJoinTask<Stream<File>>> dirTasks = dirs.map(subdir -> new DirWalker(subdir, name).fork());
            dirTasks.forEach(tasks::add);

            return tasks.stream().flatMap(t -> t.join());
        }

        private static <E> List<E> toList(E[] a) {
            if (a == null) {
                return Collections.emptyList();
            } else {
                return Arrays.asList(a);
            }
        }
    }

    static class FileLooker extends RecursiveTask<Stream<File>> {
        private Stream<File> files;
        private String name;

        public FileLooker(Stream<File> files, String name) {
            this.files = files;
            this.name = name;
        }

        @Override
        protected Stream<File> compute() {
            return files.filter((File f) -> f.getName().contains(name));
        }
    }

    @Test
    public void recursively() {
        parseAllFiles("C:/", "ubs");
        System.out.println("Done");
    }

    public void parseAllFiles(String parentDirectory, String searchword) {
        File[] filesInDirectory = new File(parentDirectory).listFiles();
        if (filesInDirectory == null) {
            return;
        }

        for (File f : filesInDirectory) {
            if (f.isDirectory()) {
                parseAllFiles(f.getAbsolutePath(), searchword);
            } else if (f.getName().contains(searchword)) {
                System.out.println(f);
            }
        }

    }
}
```

В этом коде два теста: один использует Fork/Join, второй обычный рекурсивный обход.


[Category:Java](Category_Java)
[Category:Java 8](Category_Java_8)
[Category:Snippets](Category_Snippets)

[Category:Concurrency](Category_Concurrency)