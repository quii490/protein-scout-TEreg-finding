---
type: protein-evaluation
gene: "CENPX"
date: 2026-06-02
tags: [protein-scout, chromatin, evaluation]
status: scored
---

## CENPX 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | CENPX / FAAP10, MHF2, STRA13 |
| 蛋白全名 | Centromere protein X |
| 蛋白大小 | 81 aa / 9.0 kDa |
| UniProt ID | A8MT69 |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32.0 | UniProt: Nucleus + Centromere/Kinetochore; GO-CC: chromatin (IDA), nucleoplasm (TAS), FANCM-MHF complex (IDA) |
| 蛋白大小 | 10/10 | ×1 | 10.0 | 81 aa, 9.0 kDa, 极小型蛋白 |
| 研究新颖性 | 10/10 | ×5 | 50.0 | PubMed strict=11, ≤20 |
| 三维结构 | 9/10 | ×3 | 27.0 | AlphaFold mean pLDDT 92.6; 13 PDB (X-ray + EM, 全蛋白高分辨) |

| 调控结构域 | 2/10 | ×2 | 4.0 | IPR018552, PF09415 — MHF/CENP-X 特异结构域; 功能域简单 |
| PPI 网络 | 7/10 | ×3 | 21.0 | Fanconi anemia + inner kinetochore 双网络; CENPS(0.999), FANCM(0.999), FANC family; IntAct 多 co-IP |
| **加权总分** | | | **144/180**** | |
| 互证加分 | | | +0.0 | |
| **归一化总分 (÷1.83)** | | | **78.7/100**** | |

### 3. 详细分析
#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt | Nucleus (ECO:0000269); Chromosome, centromere (ECO:0000269); Chromosome, centromere, kinetochore (ECO:0000269) | 高（实验证据） |
| GO-CC | chromatin (IDA:ComplexPortal), nucleoplasm (TAS:Reactome), nucleus (NAS:ComplexPortal), FANCM-MHF complex (IDA), Fanconi anaemia nuclear complex (IDA), inner kinetochore (IPI) | 高 |
| Protein Atlas (IF) | HPA 无 IF 图像（no_image_detected） | 未确认 |

**HPA IF 状态**: no_image_detected — HPA 未检测到可用 IF 图像。核定位基于 UniProt + GO-CC。

**结论**: CENPX 核定位证据非常充分。GO-CC 含 IDA 级别的 chromatin 和 FANCM-MHF complex 注释，UniProt 有 ECO:0000269 实验级别支持。定位于染色质/动粒/Fanconi anemia 核复合物，证据链多源且高质量。HPA 无 IF 图像，但在 CENPX（81 aa, 9.0 kDa）这样的小蛋白上 HPA 抗体可能难以获得。

#### 3.2 结构与数据源
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-A8MT69-F1 |
| 平均 pLDDT | 92.6 |
| pLDDT >90 | 88.9% |
| pLDDT 70-90 | 2.5% |
| PDB | 13 个结构（X-ray 1.80-7.00A + EM 2.83-12.00A），覆盖 MHF 复合物、CENP-T/W/S/X 四聚体 |
| InterPro | IPR018552 |
| Pfam | PF09415 |

**AlphaFold PAE 状态**: PAE 已下载，模型置信度极高（mean pLDDT 92.6, >90 占 88.9%）。小蛋白折叠紧凑，预测可靠性强。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 11 |
| PubMed broad | 26 |
| 别名 | FAAP10, MHF2, STRA13（未用于 scoring） |

关键文献：CENPX 文献量低（strict=11），主要为 Fanconi anemia 通路研究和 CENP family 泛癌分析。PMID:39421870（FA 突变组织特异性）、PMID:35695666（肺癌 CENP 家族表达）、PMID:31417608（糖尿病中 CENPX 沉默改善高血糖）。PMID:20347428 和 20347429 为核心功能文献，鉴定 CENPX/CENPS 为 MHF 复合物的 DNA 结合组分。PMID:19620631 发现其为 CENP-T/W/S/X 动粒组分。总体低研究热度（10/10 新颖性）。

#### 3.4 PPI 网络（三源综合）
| Partner | Source | Score/Evidence | Relevance |
|---|---|---|---|
| CENPS | STRING + IntAct | 0.999 (exp 0.999; molecular sieving) | MHF heterodimer partner |
| FANCM | STRING | 0.999 (exp 0.999) | Fanconi anemia core |
| FAAP100 | STRING | 0.999 (exp 0.994) | Fanconi anemia core |
| FANCG | STRING | 0.999 (exp 0.994) | Fanconi anemia core |
| FANCA | STRING | 0.999 (exp 0.994) | Fanconi anemia core |
| FANCL | STRING | 0.999 (exp 0.994) | Fanconi anemia core |
| FANCC | STRING | 0.999 (exp 0.994) | Fanconi anemia core |
| FAAP24 | STRING | 0.999 (exp 0.994) | Fanconi anemia core |
| CENPT | STRING | 0.999 (exp 0.896) | CENP-T/W/S/X complex |
| CENPW | STRING | 0.999 (exp 0.927) | CENP-T/W/S/X complex |

PPI 网络极其强大且实验验证充分，呈现双重身份：Fanconi anemia 核心复合物（与 FANCM/FANCA/FANCG 等高实验得分）和动粒 CENP-T/W/S/X 四聚体。IntAct 确认 CENPS（molecular sieving, PMID:22304917）、CENPH/CENPO/CENPQ/CENPU（co-IP, PMID:26496610）等物理互作。

**UniProt 记录互作**: CENPS (8 experiments), REL (3), TRIM54 (3, isoform 2)。

### 4. 总体评价
CENPX 是本批次评分最高的候选（80.0/100）。核心优势：极低文献量（PM=11）、极高 AF 置信度（pLDDT 92.6）、丰富 PDB 结构（13个高分辨）、双重核定位确认（Fanconi anemia 核心复合物 + 动粒）、极强的实验验证 PPI 网络。小蛋白（9.0 kDa）在结构研究上具有天然优势。主要弱点：结构域功能注释简单、无 HPA IF 验证。作为 chromatin 类别候选，是兼具高结构置信度和低研究热度的优质目标。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A8MT69
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A8MT69
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CENPX
- Protein Atlas: https://www.proteinatlas.org/ENSG00000169689-CENPX（无 IF 原图）


HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-A8MT69-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
