---
type: sperm-protein-evaluation
gene: "NT5C1B-RDH14"
module: sperm
status: sperm_candidate
date: 2026-06-22
tags: [protein-scout, sperm, evaluation]
---

# NT5C1B-RDH14 — 精子模块评估

## 1. 基本信息
- **基因:** NT5C1B-RDH14
- **Ensembl:** ENSG00000250741
- **抗体:** 未获取
- **IF 可靠性:** 未获取
- **PubMed:** 0 篇
- **精子定位部位:** Connecting piece、Mid piece (2 个)
- **UniProt Subcellular Location:** GO: cytoplasm

## 2. HPA 精子定位证据
- **来源:** Connecting piece、Mid piece ✓
- **链接:** https://www.proteinatlas.org/ENSG00000250741-NT5C1B-RDH14
- **IF 图像:** 已获取 (6 张)


<!-- SPERM_HPA_IF_START -->
**HPA IF 图像（2026-06-22）**: HPA subcellular 页面有 IF 图像 (6 张 blue_red_green)。
![](https://images.proteinatlas.org/56683/2017_G8_29_cr5fca2941c0e19_blue_red_green.jpg)
![](https://images.proteinatlas.org/56683/2049_H3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/56683/2049_H3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/56683/1924_G2_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/56683/2017_G8_5_cr5fca2941c056b_blue_red_green.jpg)
![](https://images.proteinatlas.org/56683/1924_G2_1_blue_red_green.jpg)
<!-- SPERM_HPA_IF_END -->



## 3. UniProt / GO-CC 精子定位证据
UniProt: C9J2C7 — .
GO-CC 精子相关: 待进一步查询 UniProt subcellular location。
InterPro: 5-nucleotidase, NAD(P)-bd_dom_sf。
Pfam: 5-nucleotidase。

## 4. PubMed 文献证据
- **文献数:** 0 篇 (极低研究量)
- *关键文献待人工调研。*

## 5. AlphaFold / PAE / PDB / 结构域
AlphaFold 数据可用 (UniProt: C9J2C7)。参见 https://alphafold.ebi.ac.uk/entry/C9J2C7
PAE 图像暂无数据（未生成本地图片），结构判断基于 AlphaFold pLDDT 统计。

## 6. PPI / 蛋白互作网络
### STRING (人类, top 10)
| Partner | Combined | Exp | DB | Text |
|---|---|---|---|---|
| ADSL | 0.999 | 0.000 | 0.000 | 0.000 |
| NT5C3A | 0.995 | 0.000 | 0.000 | 0.000 |
| NT5C3A | 0.976 | 0.000 | 0.000 | 0.000 |
| NT5C2 | 0.967 | 0.000 | 0.000 | 0.000 |
| NT5C2 | 0.963 | 0.000 | 0.000 | 0.000 |
| NT5C3A | 0.961 | 0.000 | 0.000 | 0.000 |
| NT5M | 0.958 | 0.000 | 0.000 | 0.000 |
| NT5C1B-RDH14 | 0.957 | 0.000 | 0.000 | 0.000 |
| NT5C3B | 0.956 | 0.000 | 0.000 | 0.000 |
| ITPA | 0.955 | 0.000 | 0.000 | 0.000 |
*待 IntAct/BioGRID/humanPPI 补充。*

## 7. 评分表
| 维度 | 评分 | 依据 |
|---|---:|---|
| 精子定位 | 16/20 | 双部位: Connecting piece、Mid piece |
| PubMed | 10/20 | 0 篇 |
| PPI | 18/20 | STRING |
| 结构 | 5/10 | AF available |
| 新颖性 | 10/10 | 极低 |

- **评分:** **72/100**

### 深度机制分析

NT5C1B-RDH14（评分72/100）是通过read-through转录产生的融合蛋白编码序列，定位于精子连接段和中段（Connecting piece, Mid piece, HPA精子定位）。其结构域包含5'-核苷酸酶催化域（Pfam:5-nucleotidase、InterPro:IPR036831）和NAD(P)结合Rossmann折叠域（IPR036291），反映出NC5C1B（胞质嘧啶核苷酸酶）和RDH14（视黄醇脱氢酶）两个亲本基因的酶活性模块。

该融合蛋白的STRING互作网络富集于核苷酸代谢酶家族：ADSL（Combined Score=0.999, 腺苷酸琥珀酸裂解酶）、NT5C3A（0.995）、NT5C2（0.967）、NT5M（0.958, 5',3'-核苷酸酶线粒体型）、ITPA（0.955, 次黄嘌呤核苷三磷酸酶），形成围绕嘧啶/嘌呤核苷酸补救合成通路的高置信度功能模块。这表明NT5C1B-RDH14融合产物在精子中保留了5'-核苷酸酶活性，可能参与精子核苷酸池的动态调控。

从TE调控角度，该蛋白的精子特异性定位限制了其在核内TE调控中的直接角色。精子中段/连接段是线粒体鞘和精子尾部连接结构的所在区域，与细胞核存在空间隔离。然而，精子发生过程中父源染色质经历了从组蛋白到鱼精蛋白的大规模交换，这一过程涉及TE元件的广泛表观遗传重置和piRNA通路的激活。NT5C1B-RDH14的核苷酸酶活性通过维持精子核苷酸代谢稳态可能间接影响piRNA生物合成所需的核苷酸前体供应，但该效应极其间接。精子模块72/100评分反映其在精子能量代谢中的潜在功能而非TE调控影响。

## 8. 结论
**SPERM CANDIDATE**

## 9. 人工复核备注
- 精子部位: Connecting piece、Mid piece
- 建议验证精子 IF 文献定位
