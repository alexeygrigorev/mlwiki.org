---
title: Dot Graph Examples
layout: default
permalink: /index.php/Dot_Graph_Examples
---

# Dot Graph Examples

## Dot Graph Examples

### Triangle
A triangle with large margins

```text only
digraph A {

  rankdir=LR;
  center=true; margin=1; 
  nodesep=1.5; ranksep=0.5;

  node [shape=point,  height=".2", width=".2"];

  a [xlabel="a"];
  b [xlabel="b"];
  c [xlabel="c"];
  a -> b -> c;
  a -> c;
}
```

<img src="http://i.stack.imgur.com/ibImr.png" alt="Image">


### Label + XLabel
```text only
digraph A {

  rankdir=LR;
  center=true; margin=1; 
  nodesep=1.5; ranksep=1.5;

  node [height="0.5", width="0.5", fixedsize=true];
  
  X [xlabel=100];
  Y [xlabel=150];
  I1 [xlabel=150];
  I2 [xlabel=100];
  {X, Y}->{I1, I2};

}
```

<img src="http://habrastorage.org/files/380/2a0/b41/3802a0b414354ad58397d8a0ebfd0771.png" alt="Image">


### Edges with Opposite Direction
Source: [http://stackoverflow.com/a/4671684/861423]

```text only
digraph A {
  rankdir=LR;
  center=true; margin=1; 

  node [height="0.33", width="0.33", fixedsize=true];

  b->a->d->g;
  a->e->h;
  e->g;
  d->{c,f};

  c->e [dir="back"];
  g->h [dir="back"];

  b,d,e [style=filled, fillcolor=red, peripheries=2];

  {rank=same; f;g;h;}
  {rank=same; d;e;c;}
  {rank=same; a;b;}
}
```

<img src="http://habrastorage.org/files/ddb/cf5/f66/ddbcf5f668c94490a91a563fcfcd3515.png" alt="Image">


### Neato Example
```text only
graph G {
  nodesep=1.5;
  center=true; margin=1; 
  node [color=black, shape=rectangle, style="filled", fillcolor=skyblue];
  edge [len=2];
  a;b;c;d;e;
  a--{b,c,d,e};
  b--{c,d,e};
  c--{d,e};
  d--e;
}
```

<img src="http://habrastorage.org/files/4aa/a61/9d5/4aaa619d5eb6433a812eee3759c82efa.png" alt="Image">


### Double Edge
Source: [http://stackoverflow.com/questions/6219933/how-does-one-define-double-lines-for-edge-and-node-shapes-in-graphviz-dot]

```text only
digraph G {
  rankdir=LR;
  nodesep=0.7; ranksep=1;
  node [shape=none, fixedsize=true, width=0.3];

  a->b->d;
  a->c->d;
  b->c [color="black:white:black",dir=none];
  a->e->d;
  c->e [style=invis];
  {rank=same;b;c;e;}
}
```

<img src="http://habrastorage.org/files/f84/5d8/269/f845d826920c4289ae0376767482c798.png" alt="Image">


[Category:Dot](Category_Dot)
[Category:Snippets](Category_Snippets)