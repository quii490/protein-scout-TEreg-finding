---
type: protein-evaluation
gene: "CHAF1B"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## CHAF1B 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | CHAF1B / CAF1A, CAF1P60, MPHOSPH7, MPP7 |
| 蛋白全名 | Chromatin assembly factor 1 subunit B |
| 蛋白大小 | 559 aa / 61.5 kDa |
| UniProt ID | Q13112 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | UniProt Nucleus (ECO:0000269)；GO-CC chromatin IDA, nucleoplasm IDA, CAF-1 complex IDA；HPA Supported, Nucleoplasm (sole location) |
| 蛋白大小 | 5/10 | ×1 | 5.0 | 559 aa, 61.5 kDa，中等大小染色质组装因子 |
| 研究新颖性 | 8/10 | ×5 | 40.0 | PubMed strict=36, broad=105 |
| 三维结构 | 7/10 | ×3 | 21.0 | AlphaFold pLDDT 74.7 (pct>90: 51.2%)；PDB 11 个结构 (X-ray+EM) |

| 调控结构域 | 8/10 | ×2 | 16.0 | WD40 repeats (IPR001680, PF15512)；CAF-1 复合体，组蛋白 H3/H4 chaperone，直接参与 DNA replication-coupled 核小体组装 |
| PPI 网络 | 7/10 | ×3 | 21.0 | STRING: CHAF1A (0.999 exp 0.898), RBBP4 (0.999 exp 0.899), ASF1B (0.993 exp 0.97)；IntAct 15 条；UniProt 2 条 |
| **加权总分** | | | **135/180**** | |
| 互证加分 | | | +0.0 | |
| **归一化总分 (÷1.83)** | | | **73.8/100**** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus (ECO:0000269), Cytoplasm (ECO:0000269) | 中高 |
| GO-CC | CAF-1 complex (IDA:UniProtKB), chromatin (IDA:UniProtKB), nucleoplasm (IDA:HPA), nucleus (IBA:GO_Central), cytoplasm (NAS:UniProtKB) | 高 |
| Protein Atlas (IF) | HPA Supported, Nucleoplasm (sole location), 无其他定位 | 中高 |

**HPA IF 状态**: HPA IF 图像已本地嵌入。

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/CHAF1B/IF_images/CHAF1B_IF_234_H9_1_red_green.jpg]]。核定位基于HPA localization/reliability + UniProt + GO-CC。


**结论**: CHAF1B 是典型的核质/染色质蛋白。GO-CC IDA 证据包括 chromatin (直接实验证据) 和 CAF-1 complex (实验证据)，HPA 单一 Nucleoplasm 定位确认核定位。核定位证据充分且高度特异。

#### 3.2 结构与数据源
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q13112-F1 |
| 平均 pLDDT | 74.7 |
| pLDDT >90 | 51.2% |
| pLDDT 70-90 | 12.2% |
| pLDDT <50 | 28.4% |
| PDB | 11 个 (7Y5K/X-ray 3.48A, 7Y5L/X-ray 3.42A, 7Y5O/X-ray 3.57A, 7Y5U/EM 3.80A, 7Y5V/EM 6.10A, 7Y60/EM 3.80A, 7Y61/EM 5.60A, 8IQF/EM 4.60A, 8IQG/EM 3.50A, 8J6S/EM 3.80A, 8J6T/EM 6.60A)，覆盖大部分蛋白 (aa 1-419 或 1-559) |
| InterPro | IPR055410, IPR029129, IPR045145, IPR015943 (WD40/YVTN repeat-like), IPR001632 (G-protein beta WD-40 repeat), IPR019775 (WD40 repeat), IPR036322, IPR001680 (WD40 repeat) |
| Pfam | PF24105, PF15512 (CAF1-p60-N) |

**AlphaFold PAE 状态**: PAE 已下载。pLDDT 中等偏上 (74.7, 51.2% >90)，28.4% <50 提示存在部分无序区域。PDB 拥有 CAF-1 全复合体 Crystal/Cryo-EM 结构，覆盖大部分蛋白。


#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 36 |
| PubMed broad | 105 |
| 别名 | CAF1A, CAF1P60, MPHOSPH7, MPP7（未用于 scoring） |

关键文献：CHAF1B 是 chromatin assembly factor 1 (CAF-1) 的核心亚基，作为组蛋白 H3/H4 chaperone 在 DNA 复制耦联的核小体组装中发挥关键功能。代表性文献：PMID:26066981 (CAF-1/p60 在 homeostasis/disease 中的角色综述), PMID:39862337 (CHAF1B 在 lung SCC 中通过 SETD7 促进进展), PMID:33575221 (CHAF1B 在 HCC 中的自噬/预后标志物), PMID:37377894 (靶向 CHAF1B 增强 IFN 在 MPN 中的活性)。文献量中低（strict=36），属于相对新颖但已有肿瘤生物学关注的染色质因子。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| CHAF1A | STRING+IntAct | 0.999 (exp 0.898), confocal microscopy colocalization | CAF-1 complex subunit A |
| RBBP4 | STRING+IntAct | 0.999 (exp 0.899), Co-IP | CAF-1 complex, histone chaperone |
| ASF1B | STRING+IntAct+UniProt | 0.993 (exp 0.97), Co-IP, 7 exp | Histone H3/H4 chaperone |
| ASF1A | STRING+UniProt | 0.988 (exp 0.937), 3 exp | Histone H3/H4 chaperone |
| H3C1/H4C6 | STRING+IntAct | 0.918/0.929 (exp 0.901/0.855), Co-IP | Histone H3/H4 substrates |
| PCNA | STRING | 0.933 (exp 0.884) | DNA replication sliding clamp |
| CBX5 | STRING | 0.911 (exp 0.858) | HP1, chromatin silencing |
| RBBP7 | STRING | 0.903 (exp 0.757) | Histone chaperone |
| MYC | IntAct | TAP (PMID:21150319) | Transcription factor |
| PDPK1 | IntAct | Co-IP (PMID:31980649) | Kinase |

PPI 网络以 CAF-1 染色质组装复合体（CHAF1A-RBBP4-ASF1A/B）为核心，实验互作高置信度（exp >0.89, Co-IP/Y2H 验证）。Histone H3/H4 (H3C1/H4C6) 的 Co-IP 验证充分。与 PCNA 互作（0.884 exp）支持其 DNA replication-coupled chromatin assembly 功能。三条数据源（STRING + IntAct + UniProt）高度一致。

### 4. 总体评价
CHAF1B 是 chromatin assembly factor 1 的核心 p60 亚基，在 DNA 复制耦联核小体组装中发挥基础性染色质功能。优势：染色质定位高度特异（GO chromatin IDA + HPA Nucleoplasm sole），调控结构域与染色质直接相关（WD40 repeats + histone chaperone），PPI 网络丰富且三源一致（CHAF1A-RBBP4-ASF1A/B 核心复合体），文献量中低（strict=36）。主要不足：分子量中等偏大 (61.5 kDa)，AlphaFold pLDDT 中等 (74.7)，28.4% 无序区域。综合评分在 nucleoplasm 类别中具有较强的竞争力。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13112
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13112
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHAF1B
- Protein Atlas: https://www.proteinatlas.org/ENSG00000159259-CHAF1B


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13112-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13112 |
| SMART | SM00320; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR055410;IPR029129;IPR045145;IPR015943;IPR001632;IPR019775;IPR036322;IPR001680; |
| Pfam | PF24105;PF15512; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000159259-CHAF1B/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ASF1A | Intact, Biogrid | true |
| ASF1B | Intact, Biogrid, Bioplex | true |
| CBX1 | Biogrid, Opencell | true |
| CBX5 | Biogrid, Bioplex | true |
| CHAF1A | Biogrid, Bioplex | true |
| H3C1 | Biogrid, Bioplex | true |
| H3C2 | Biogrid, Bioplex | true |
| H3C3 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
