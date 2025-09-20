---
title: "Playground"
layout: default
permalink: /index.php/Playground
---

# Playground

Conjunctie query

$ 
\begin{array}{l l}
Q(\text{$E_1$.eid}) \leftarrow & \text{Emp}(\text{$E$.eid}, \text{$E$.did}, \text{$E$.sal}, \text{$E$.hobby}), \\
& \text{Emp}(\text{$E_1$.eid}, \text{$E_1$.did}, \text{$E_1$.sal}, \text{$E_1$.hobby}), \\
& \text{Emp}(\text{$E_2$.eid}, \text{$E_2$.did}, \text{$E_2$.sal}, \text{$E_2$.hobby}), \\
& \text{Dept}(\text{$D_1$.did}, \text{$D_1$.dname}, \text{$D_1$.floor}, \text{$D_1$.phone}), \\
& \text{Dept}(\text{$D_2$.did}, \text{$D_2$.dname}, \text{$D_2$.floor}, \text{$D_2$.phone}), \\
& \text{Finance}(\text{$F$.did}, \text{$F$.budget}, \text{$F$.sales}, \text{$F$.expenses}) \\
\end{array}
$


$R^k_{ij} = \color{grey}{\underbrace{\{\color{black}\{ \ R^{k-1}_{ij} \ \}\}}_{\small\text{(1)}} \{\color{black}\{+\}\} \underbrace{\{\color{black}\{ \ R^{k-1}_{ik}  \  \}\}}_{\small\text{(2)}} \underbrace{\{\color{black}\{  \  \big( R^{k-1}_{kk} \big)^*  \  \}\}}_{\small\text{(3)}} \underbrace{\{\color{black}\{  \  R^{k-1}_{kj}  \  \} \}}_{\small\text{(4)}}}$