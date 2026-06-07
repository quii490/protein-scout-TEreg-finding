---
type: protein-evaluation
gene: "TMTC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TMTC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TMTC1 |
| 蛋白名称 | Protein O-mannosyl-transferase TMTC1 |
| 蛋白大小 | 882 aa / 98.8 kDa |
| UniProt ID | Q8IUR5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Cytosol; UniProt: Membrane; Endoplasmic reticulum |
| 蛋白大小 | 8/10 | ×1 | 8 | 882 aa / 98.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=87.7; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR003107, IPR013618, IPR052943, IPR011990, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **114.5/180** | |
| **归一化总分** | | | **63.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Membrane; Endoplasmic reticulum | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- membrane (GO:0016020)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Global View of Domain-Specific O-Linked Mannose Glycosylation in Glycoengineered Cells.. *Molecular & cellular proteomics : MCP*. PMID: 38851451
2. Multiple distinct O-Mannosylation pathways in eukaryotes.. *Current opinion in structural biology*. PMID: 30999272
3. TMTC1 promotes invasiveness of ovarian cancer cells through integrins β1 and β4.. *Cancer gene therapy*. PMID: 37221403
4. Identification of potential key targets and mechanisms underlying cleft palate induced by tobacco smoke exposure through multi-omics integrated Mendelian randomization analysis.. *Ecotoxicology and environmental safety*. PMID: 40435780
5. Endothelial-specific genes TMTC1, RPS6KA2, and F8 are downregulated in hypertrophic cardiomyopathy.. *European journal of medical research*. PMID: 41392291

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.7 |
| 高置信度残基 (pLDDT>90) 占比 | 78.5% |
| 置信残基 (pLDDT 70-90) 占比 | 8.7% |
| 中等置信 (pLDDT 50-70) 占比 | 2.7% |
| 低置信 (pLDDT<50) 占比 | 10.1% |
| 有序区域 (pLDDT>70) 占比 | 87.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=87.7，有序区 87.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003107, IPR013618, IPR052943, IPR011990, IPR013105; Pfam: PF08409, PF13424, PF13432 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DRD1 | 0.920 | 0.000 | — |
| GNAL | 0.873 | 0.000 | — |
| EBF1 | 0.852 | 0.000 | — |
| EBF2 | 0.847 | 0.000 | — |
| EBF4 | 0.817 | 0.000 | — |
| OMP | 0.793 | 0.000 | — |
| RIC8B | 0.784 | 0.000 | — |
| GRHPR | 0.768 | 0.000 | — |
| ADORA2A | 0.728 | 0.000 | — |
| ADCY3 | 0.714 | 0.046 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| JPH2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| ZDHHC17 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-21827|pubmed:24705354 |
| HTT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| WFS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| KIF1B | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| BACE2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| KLF11 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| NUP58 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| KCNIP3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| KLK6 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.7 + PDB: 无 | pLDDT=87.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane; Endoplasmic reticulum / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TMTC1 — Protein O-mannosyl-transferase TMTC1，非常新颖，仅有少数基础研究。
2. 蛋白大小882 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IUR5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000133687-TMTC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TMTC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IUR5
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000133687-TMTC1/subcellular

![](https://images.proteinatlas.org/16720/133_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/16720/133_D3_2_red_green.jpg)
![](https://images.proteinatlas.org/16720/134_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/16720/134_D3_2_red_green.jpg)
![](https://images.proteinatlas.org/16720/135_D3_1_red_green.jpg)
![](https://images.proteinatlas.org/16720/135_D3_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IUR5-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IUR5 |
| SMART | SM00386;SM00028; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR003107;IPR013618;IPR052943;IPR011990;IPR013105;IPR019734; |
| Pfam | PF08409;PF13424;PF13432;PF14559;PF07719; |

### humanPPI / HPA Interaction
Source: 未找到 HPA interaction 页面

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
