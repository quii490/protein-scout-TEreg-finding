---
type: protein-evaluation
gene: "NANP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NANP — REJECTED (研究热度过高 (PubMed strict=252，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NANP / C20orf147, HDHD4 |
| 蛋白名称 | N-acylneuraminate-9-phosphatase |
| 蛋白大小 | 248 aa / 27.8 kDa |
| UniProt ID | Q8TBE9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Cytosol; 额外: Nuclear membrane; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 248 aa / 27.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=252 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=94.8; PDB: 2W4M, 4KNV, 4KNW |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051400, IPR036412, IPR006439, IPR011950, IPR023 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.0/180** | |
| **归一化总分** | | | **45.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nuclear membrane | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 252 |
| PubMed broad count | 514 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C20orf147, HDHD4 |

**关键文献**:
1. Safety and efficacy of malaria vaccine candidate R21/Matrix-M in African children: a multicentre, double-blind, randomised, phase 3 trial.. *Lancet (London, England)*. PMID: 38310910
2. mRNA delivery of circumsporozoite protein epitope-based malaria vaccines induces protection in a mouse model.. *NPJ vaccines*. PMID: 41253879
3. Repertoire, function, and structure of serological antibodies induced by the R21/Matrix-M malaria vaccine.. *The Journal of experimental medicine*. PMID: 40719751
4. Natural Parasite Exposure Induces Protective Human Anti-Malarial Antibodies.. *Immunity*. PMID: 29195810
5. Structural and biophysical correlation of anti-NANP antibodies with in vivo protection against P. falciparum.. *Nature communications*. PMID: 33594061

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.8 |
| 高置信度残基 (pLDDT>90) 占比 | 88.3% |
| 置信残基 (pLDDT 70-90) 占比 | 8.5% |
| 中等置信 (pLDDT 50-70) 占比 | 2.4% |
| 低置信 (pLDDT<50) 占比 | 0.8% |
| 有序区域 (pLDDT>70) 占比 | 96.8% |
| 可用 PDB 条目 | 2W4M, 4KNV, 4KNW |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2W4M, 4KNV, 4KNW）+ AlphaFold高质量预测（pLDDT=94.8），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051400, IPR036412, IPR006439, IPR011950, IPR023214; Pfam: PF00702 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NANS | 0.976 | 0.000 | — |
| CMAS | 0.963 | 0.000 | — |
| RSPH3 | 0.956 | 0.954 | — |
| NEU1 | 0.780 | 0.000 | — |
| GNE | 0.775 | 0.000 | — |
| PSAT1 | 0.744 | 0.000 | — |
| NT5E | 0.742 | 0.000 | — |
| TBC1D24 | 0.695 | 0.000 | — |
| KLHL3 | 0.627 | 0.514 | — |
| NPPA | 0.603 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dmel\CG10600 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| "BEST:GH09876" | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Cpr64Ad | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| cup | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG15631 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Rop | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dd | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| SmydA-3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Mst84Dd | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| EBI-109018 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.8 + PDB: 2W4M, 4KNV, 4KNW | pLDDT=94.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | 无注释 / Cytosol; 额外: Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NANP — N-acylneuraminate-9-phosphatase，研究基础较多，新颖性有限。
2. 蛋白大小248 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 252 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 252 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TBE9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000170191-NANP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NANP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TBE9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (approved)。来源: https://www.proteinatlas.org/ENSG00000170191-NANP/subcellular

![](https://images.proteinatlas.org/50342/739_A10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/50342/739_A10_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/50342/753_A10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50342/753_A10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/50342/837_E2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/50342/837_E2_5_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8TBE9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
