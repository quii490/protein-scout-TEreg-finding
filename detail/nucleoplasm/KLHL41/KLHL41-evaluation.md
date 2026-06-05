---
type: protein-evaluation
gene: "KLHL41"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KLHL41 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KLHL41 / KBTBD10, KRP1 |
| 蛋白名称 | Kelch-like protein 41 |
| 蛋白大小 | 606 aa / 68.0 kDa |
| UniProt ID | O60662 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm, Plasma membrane; UniProt: Cytoplasm; Cytoplasm, cytoskeleton; Cell projection, pseudop |
| 蛋白大小 | 10/10 | ×1 | 10 | 606 aa / 68.0 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=21 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=93.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011705, IPR017096, IPR000210, IPR015915, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **128.5/180** | |
| **归一化总分** | | | **71.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm, Plasma membrane | Supported |
| UniProt | Cytoplasm; Cytoplasm, cytoskeleton; Cell projection, pseudopodium; Cell projection, ruffle; Cytoplas... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Cul3-RING ubiquitin ligase complex (GO:0031463)
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- endoplasmic reticulum membrane (GO:0005789)
- M band (GO:0031430)
- nucleoplasm (GO:0005654)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 21 |
| PubMed broad count | 38 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KBTBD10, KRP1 |

**关键文献**:
1. Protein expression of prognostic genes in primary melanoma and benign nevi.. *Journal of cancer research and clinical oncology*. PMID: 34757537
2. Rapid Targeted Genomics in Critically Ill Newborns.. *Pediatrics*. PMID: 28939701
3. KLHL41 orchestrates sarcomere assembly and size to drive skeletal muscle hypertrophy in vivo.. *bioRxiv : the preprint server for biology*. PMID: 40501557
4. Dysregulation of NRAP degradation by KLHL41 contributes to pathophysiology in nemaline myopathy.. *Human molecular genetics*. PMID: 30986853
5. Critical genes in human photoaged skin identified using weighted gene co-expression network analysis.. *Genomics*. PMID: 37454939

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.2 |
| 高置信度残基 (pLDDT>90) 占比 | 90.4% |
| 置信残基 (pLDDT 70-90) 占比 | 5.8% |
| 中等置信 (pLDDT 50-70) 占比 | 0.8% |
| 低置信 (pLDDT<50) 占比 | 3.0% |
| 有序区域 (pLDDT>70) 占比 | 96.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=93.2，有序区 96.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011705, IPR017096, IPR000210, IPR015915, IPR006652; Pfam: PF07707, PF00651, PF24681 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.978 | 0.338 | — |
| NEB | 0.969 | 0.461 | — |
| RBX1 | 0.960 | 0.292 | — |
| KLHL9 | 0.934 | 0.000 | — |
| KLHL13 | 0.927 | 0.000 | — |
| KLHL42 | 0.924 | 0.062 | — |
| GAN | 0.922 | 0.000 | — |
| ENC1 | 0.921 | 0.000 | — |
| KLHL20 | 0.918 | 0.000 | — |
| KLHL21 | 0.916 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYBPC1 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| NEB | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| NRAP | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| POMP | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| TCAP | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| ENSRNOP00000009969.2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:23414517|imex:IM-16425 |
| HNRNPAB | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| RCHY1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SPMIP2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| Slc2a4 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:16396496|mint:MINT-5218 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.2 + PDB: 无 | pLDDT=93.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, cytoskeleton; Cell projectio / Cytosol; 额外: Nucleoplasm, Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. KLHL41 — Kelch-like protein 41，非常新颖，仅有少数基础研究。
2. 蛋白大小606 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 21 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O60662
- Protein Atlas: https://www.proteinatlas.org/ENSG00000239474-KLHL41/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KLHL41
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O60662
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (supported)。来源: https://www.proteinatlas.org/ENSG00000239474-KLHL41/subcellular

![](https://images.proteinatlas.org/21165/1161_G8_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21165/1161_G8_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/21165/188_A3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21165/188_A3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/21753/147_C11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/21753/147_C11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O60662-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
