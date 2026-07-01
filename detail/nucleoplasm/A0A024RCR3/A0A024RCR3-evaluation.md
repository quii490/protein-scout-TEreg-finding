---
type: protein-evaluation
gene: "A0A024RCR3"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## A0A024RCR3 (MHC class I alpha chain) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | A0A024RCR3 |
| 蛋白全称 | MHC class I alpha chain |
| UniProt ID | A0A024 |
| 蛋白大小 | 354 aa / 38.9 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | no known nuclear annotation |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16.0 | no known nuclear annotation |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 354 aa |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed=0; TrEMBL entry |
| 三维结构 | 6/10 | ×3 | 18.0 | AF pLDDT available; no experimental PDB |
| 调控结构域 | 8/10 | ×2 | 16.0 | InterPro:IPR007110; InterPro:IPR036179; InterPro:IPR013783; InterPro:IPR003006; InterPro:IPR003597; InterPro:IPR050208 |
| PPI | 5/10 | ×3 | 15.0 | PPI data limited |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

Involved in the presentation of foreign antigens to the immune system

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR007110 |
| InterPro | IPR036179 |
| InterPro | IPR013783 |
| InterPro | IPR003006 |
| InterPro | IPR003597 |
| InterPro | IPR050208 |
| InterPro | IPR011161 |
| InterPro | IPR037055 |

#### 3.3 核定位

no known nuclear annotation

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/A0A024RCR3

### 深度机制分析

A0A024RCR3同样共享MHC I类α链的Ig样结构域和抗原识别结构域组合，但其PPI网络是所有6个同类蛋白中最具转录调控特征的——完全由同源异形盒（homeobox, HOX）转录因子及其辅因子构成：HOXA5（score 420）、HOXB7（494）、HOXA10（597）、HOXA9（650）、HOXC9（539）、TLX1（617）、LMX1B（493）和MAB21L1（872），以及TALE（Three Amino acid Loop Extension）类同源域辅因子PKNOX1（433，又称PREP1）、PKNOX2（712，又称PREP2）、PBX2（726）和MEIS3（527）。HOX蛋白是后生动物体轴发育的核心调控因子，通过其高度保守的60个氨基酸同源域（homeodomain）以序列特异性方式结合DNA。TALE辅因子（PBX/MEIS/PKNOX）通过形成异源二聚体/三聚体显著增强HOX蛋白的DNA结合亲和力和序列特异性，将原本纳摩尔级别的低亲和力转化为皮摩尔级别的高亲和力。PBX2（score 726）和PKNOX2（score 712）的高分互作尤其值得注意，表明A0A024RCR3可能位于HOX-TALE复合体组装的核心节点，而非边缘伙伴。

HOX转录因子直接参与TE调控的实验证据近年已逐渐积累。HOXA10已被证实在子宫内膜间质细胞中介导孕酮驱动的HERV-K LTR逆转录转座子激活（PMID: 28696217），这一调控在胚胎着床窗口期发挥关键的生理功能。HOXB家族成员（包括HOXB7）已被报道与ERV-L和MER家族重复元件的表达水平相关。LMX1B（LIM同源域转录因子）虽然主要研究集中于肾脏和肢体发育，但其LIM结构域的蛋白-蛋白相互作用能力可能赋予其在TE调控中的独特角色。NOTCH4（score 626）的存在进一步丰富了这一调控画面——Notch信号通路的胞内结构域（NICD）在γ-分泌酶切割后转位至细胞核，与CSL/RBP-J转录因子形成复合体激活靶基因，而Notch和HOX信号通路在多个发育场景中存在交叉调控（cross-regulation）。

A0A024RCR3与密集的HOX因子互作暗示了一种全新的调控模型：该MHC样蛋白可能作为同源域转录因子的选择性共调节因子（co-modulator）。MHC I类折叠中的α1和α2结构域形成的肽结合沟，在经典免疫学功能中高度多态且与抗原肽和TCR相互作用。但在核内环境中，这个肽结合沟可能被重新利用（exapted）以识别HOX蛋白或其修饰状态，从而选择性地增强或抑制特定HOX-TALE复合体对下游靶基因（包括TE）的调控。SLC38A2（SNAT2, score 760）——一个谷氨酰胺转运体——的参与可能提供了代谢-转录耦联的线索：谷氨酰胺是mTORC1信号通路的关键激活信号，而mTORC1已知可以调控HOX基因表达和整体翻译活性。

实验验证应聚焦于：(1) 邻近依赖性生物素化（BioID/TurboID）实验绘制其在核内的全互作组图谱；(2) 荧光素酶报告基因实验，利用含有HOX响应元件和TE启动子序列的报告系统，逐一检测A0A024RCR3对各HOX因子转录活性的影响；(3) 染色质免疫共沉淀（ChIP-seq）以确定其与HOX结合位点、特别是TE相关HOX结合位点的共占据模式；(4) CRISPR knockout或CRISPRa/CRISPRi扰动后RNA-seq，区分其在HOX调控网络中的正负调控方向及对TE家族表达的整体影响。

### 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A0A024
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A0A024
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=A0A024RCR3

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| HOXA5 | STRING | 420 |
| HOXB7 | STRING | 494 |
| SLC38A2 | STRING | 760 |
| HOXA10 | STRING | 597 |
| PKNOX1 | STRING | 433 |
| PKNOX2 | STRING | 712 |
| HOXA9 | STRING | 650 |
| LMX1B | STRING | 493 |
| TLX1 | STRING | 617 |
| NOTCH4 | STRING | 626 |
| PBX2 | STRING | 726 |
| MAB21L1 | STRING | 872 |
| HOXC9 | STRING | 539 |
| MEIS3 | STRING | 527 |

### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000204304

![](https://images.proteinatlas.org/61478/1261_A11_1_red_green.jpg)
![](https://images.proteinatlas.org/61478/1261_A11_3_red_green.jpg)
![](https://images.proteinatlas.org/61478/1148_C10_3_red_green.jpg)
![](https://images.proteinatlas.org/61478/1148_C10_4_red_green.jpg)
![](https://images.proteinatlas.org/61478/1106_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/61478/1106_C10_3_red_green.jpg)
