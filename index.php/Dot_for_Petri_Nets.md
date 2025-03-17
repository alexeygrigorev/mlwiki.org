---
title: Dot for Petri Nets
layout: default
permalink: /index.php/Dot_for_Petri_Nets
---

# Dot for Petri Nets

Dot for [Petri Nets](Petri_Nets)

## Simplest Petri Net
```text only
digraph G {
  rankdir=LR;
  center=true; margin=1; 
  subgraph place {
    node [shape=circle,fixedsize=true,label="", height=.3,width=.3];
    # i [label="&bull;", fontsize=20];
    p1, p2;
  }
  subgraph transitions {
    node [shape=rect,height=0.4,width=.4];
    t1 [label=<t<SUB>1</SUB>>];
  }
  
  p1->t1->p2;
}
```

<img src="http://habrastorage.org/files/5f9/02c/cbd/5f902ccbdb4243f0b8ded50791a67159.png" alt="Image">


## Nodes Alignment
```text only
digraph G {
  rankdir=LR;
  subgraph place {
    node [shape=circle,fixedsize=true,label="",height=.3,width=.3];
    i [label="&amp;bull;", fontsize=20];
    o; p1; p2;
  }
  subgraph transitions {
    node [shape=rect,height=0.4,width=.4];
    a; b; c; d; e; f;
  }

  # align horizontally
  {edge [weight=2]; i->a->p1; p2->f->o;}

  p1->c->p2;
  p2->d->p1;
  i->e->p2;
  p1->b->o; 
  # align vertically
  {rank=same; b;c;d;e;}  
}
```

<img src="http://habrastorage.org/files/2b5/6cf/d24/2b56cfd24a924d05b6e4d823971535cd.png" alt="Image">


## Red Color and Alignment
```text only
digraph G {
  rankdir=LR;
  ranksep=0.3;
  subgraph place {
    node [shape=circle,fixedsize=true,label=" ",height=.3,width=.3];
    i [label="&amp;bull;", fontsize=20];
    p6 [color=red];
    o; p1; p2; p3; p4; p5; 
  }
  subgraph transitions {
    node [shape=rect,height=.4,width=.4];
    a; b; c; d; e; f;
  }

  i -> a -> p1 -> b -> p3 -> d -> o;
  a -> p2 -> c -> p4 -> d;
  i -> e; f->o;
  e -> p5 -> f [weight=2]; # makes it straight
  a -> p6 -> d [color=red];

  {rank=same;p5;p6;b;c;}
}
```

<img src="http://habrastorage.org/files/aa7/b07/5fe/aa7b075fe4984ae7af0640a62e52f285.png" alt="Image">


## Clusters
Using keyword <code>cluster</code> before name of a subgraph

```text only
digraph G1 {
  rankdir=LR;
  subgraph place {
    node [shape=circle,fixedsize=true,label=" ",height=.3,width=.3];
    p1;
  }
  subgraph transitions {
    style="rounded,dashed";
    color=red;
    node [shape=rect,height=.4,width=.4];
    subgraph cluster_a {
      label="A";
      a;b;        
    }
    subgraph cluster_b {
      label="B";
      c;d;
    }
  }

  {a,b}->p1->{c,d};
}
```

<img src="http://habrastorage.org/files/719/a01/946/719a019467fa4637b85191631e22abe4.png" alt="Image">


## Records
Special shape: record

```text only
digraph G1 {
  rankdir=LR;
  s1 [style="invisible", shape=record, label="<0>| <1> | <2>|<3>"]; |  s2 [style="invisible", shape=record, label="<0>| <1> | <2>|<3>"]; |  
  subgraph place {
    node [shape=circle,fixedsize=true,label=" "];
    p1;p2;
  }
  subgraph transitions {
    node [shape=rect,height=.5,width=.5];
    a;
  }

  s1:0->p1 [color=red];
  s1:1->p1;
  {p1, p2}->a;
  s1:2->p2;
  s1:3->p2 [color=red];
  a->s2:2;
  a->s2:3;
}
```

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pm/not-allowed-1.png" alt="Image">

```text only
digraph G2 {
  rankdir=LR;
  s1 [style="invisible", shape=record, label="<0>| <1> | <2>|<3>"]; |  s2 [style="invisible", shape=record, label="<0>| <1> | <2>|<3>"]; |  
  subgraph place {
    node [shape=circle,fixedsize=true,label=" "];
    p1;
  }
  subgraph transitions {
    node [shape=rect,height=.5,width=.5];
    a;b;
  }

  s1:0->a [color=red];
  s1:1->p1;
  s1:2->p1;
  p1->{a, b};
  s1:3->b [color=red];
  a->s2:0;
  a->s2:1;
  b->s2:2;
  b->s2:3;
}
```

<img src="https://raw.github.com/alexeygrigorev/wiki-figures/master/ulb/bpm/pm/not-allowed-2.png" alt="Image">

## Candy Storage (neato)
```text only
digraph G {
  center=true; margin=1; 
  normalize=true;
  subgraph place {
    node [shape=circle,fixedsize=true,label="", height=.3,width=.3];
    p1, p2, p3, p4, p5;
  }
  subgraph transitions {
    node [shape=rect,height=0.4,width=.4, rotate=90];
    refill;
    disp [label="dispence\ncandy"];
    rej [label="reject\ncoin"];
    ins [label="insert\ncoin"];
    ac [label="accept\ncoin"];
  }

  refill->p1->disp->p3->ins->p4->ac->p5->disp->p2->refill;
  p4->rej->p3;
  rej->p5 [style=invis]; 
}
```


<img src="http://habrastorage.org/files/69c/8b7/2b4/69c8b72b47f540399701f3a4ed6b6b9f.png" alt="Image">


## [Reachability Graph](Reachability_Graph)
```text only
digraph G {
  center=true; margin=1; 

  fontsize=12;
  normalize=true;
 
  edge [len=1.3, minlen=1];
  node [shape=none, fixedsize=true];

  i [label="[i]"];
  p1 [label=<&amp;#91;p<SUB>1</SUB>, p<SUB>5</SUB>&amp;#93;>];
  p2 [label=<&amp;#91;p<SUB>2</SUB>, p<SUB>5</SUB>&amp;#93;>];
  p3 [label=<&amp;#91;p<SUB>3</SUB>, p<SUB>5</SUB>&amp;#93;>];
  p4 [label=<&amp;#91;p<SUB>1</SUB>, p<SUB>6</SUB>&amp;#93;>];
  p5 [label=<&amp;#91;p<SUB>2</SUB>, p<SUB>6</SUB>&amp;#93;>];
  p6 [label=<&amp;#91;p<SUB>3</SUB>, p<SUB>6</SUB>&amp;#93;>];
  p7 [label=<&amp;#91;p<SUB>4</SUB>&amp;#93;>];
  o [label="[o]"];

  i->p1 [label=x];
  p1->p2 [label=a];
  p2->p5 [label=d];
  p5->p2 [label=e];
  p1->p3 [label=b];
  p3->p6 [label=d];
  p6->p3 [label=e];
  p1->p4 [label=d];
  p4->p1 [label=e];
  p4->p5 [label=b];
  p4->p6 [label=a];
  p7->o [style=invis];
  p4->{o, p7} [style=invis];
}
```

<img src="http://habrastorage.org/files/904/16d/d88/90416dd883c54d8c8412b31da4fe7274.png" alt="Image">


[Category:Business Process Management](Category_Business_Process_Management)
[Category:Petri Nets](Category_Petri_Nets)
[Category:Dot](Category_Dot)
[Category:Snippets](Category_Snippets)