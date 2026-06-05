---
type: protein-evaluation
gene: "GSK3A"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## GSK3A 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | GSK3A / Glycogen synthase kinase-3 alpha |
| 蛋白全名 | Glycogen synthase kinase-3 alpha |
| 蛋白大小 | 483 aa / 51.0 kDa |
| UniProt ID | P49840 |

**HPA IF 状态**: HPA Approved 级别, Nucleoplasm (main) + Cytosol (additional)。IF 图像 URL 存在于 HPA 数据库，但本地未缓存。

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | x4 | 20.0 | HPA Approved: Nucleoplasm (main) + Cytosol (additional); GO-CC: nucleus (IBA), cytoplasm/cytosol/mitochondrion/axon |
| 蛋白大小 | 7/10 | x1 | 7.0 | 483 aa, 51.0 kDa |
| 研究新颖性 | 4/10 | x5 | 20.0 | PubMed strict=80 |
| 三维结构 | 8/10 | x3 | 24.0 | PDB: 7SXF (1.94A), 7SXG (2.40A); AlphaFold pLDDT=78.9, pct>90=65.6% |
| 调控结构域 | 8/10 | x2 | 16.0 | Protein kinase domain (IPR000719); Wnt/beta-catenin 核心激酶; 磷酸化多种转录因子 |
| PPI 网络 | 9/10 | x3 | 27.0 | Massive Wnt signaling PPI: AXIN1/APC/CTNNB1/GSK3B/AKT1; IntAct: 15+ experimental partners |
| **加权总分** | | | **114/180********** | |
| 互证加分 | | | +2.0 | HPA+GO nucleus 互证; PPI: STRING+IntAct+UniProt 高度重叠 (AXIN1, GSKIP, NBR1, etc.) |
| **归一化总分 (÷1.83)** | | | **62.3/100********** | |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| HPA | Nucleoplasm (main), Cytosol (additional) | Approved |
| UniProt | 无 Subcellular Location 注释 | — |
| GO-CC | nucleus (IBA), cytoplasm (IBA), cytosol (IBA), beta-catenin destruction complex (TAS), axon, mitochondrion, etc. | — |

**结论**: HPA Approved 级别 Nucleoplasm 主定位。GSK3A 为核-胞质穿梭蛋白，Wnt 信号下核转位调控 beta-catenin。核定位有实验支持。

#### 3.2 蛋白大小评估
483 aa, 51.0 kDa。Ser/Thr 蛋白激酶，大小适中。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 80 |
| PubMed broad | 119 |
| 新颖性级别 | 有一定研究 |

PubMed 80 篇。GSK3A 是 Wnt 信号核心激酶，但研究主要集中在 GSK3B (更知名的 isoforms)。GSK3A 特异性研究方向（如 hepatocellular carcinoma immunotherapy、viral replication）仍有 niche 空间。

**关键文献**:
1. Zheng X et al. (2024). "Targeting Gsk3a reverses immune evasion to enhance immunotherapy in hepatocellular carcinoma." *J Immunother Cancer*. PMID: 39174053
2. Lin Y et al. (2025). "GSK3A promotes human adenovirus replication and phosphorylates viral L4-22K protein." *Life Sci Alliance*. PMID: 40537285
3. Park DS et al. (2023). "High-throughput Oligopaint screen identifies druggable 3D genome regulators." *Nature*. PMID: 37438531
4. Freitas MJ et al. (2019). "Isoform-specific GSK3A activity is negatively correlated with human sperm motility." *Mol Hum Reprod*. PMID: 30824926
5. McKenna JK et al. (2025). "The ubiquitin ligase HUWE1 enhances WNT signaling by antagonizing destruction complex-mediated beta-catenin degradation." *PLoS Genet*. PMID: 40424469

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-P49840-F1 v6 |
| 平均 pLDDT | 78.9 |
| pLDDT >90 | 65.6% |
| pLDDT 70-90 | 6.0% |
| pLDDT 50-70 | 1.4% |
| pLDDT <50 | 26.9% |
| PDB | 7SXF (1.94A, aa101-444), 7SXG (2.40A, aa103-445) |

**AlphaFold PAE**:

高质量结构：65.6% 区域内 >90 置信度。2 个 PDB entries 覆盖 catalytic domain (aa101-445)。N 端 (aa1-100) 为无序区域。

#### 3.5 结构域分析
| 来源 | 结构域 | 备注 |
|---|---|---|
| InterPro | IPR050591 (GSK3), IPR011009 (Kinase-like), IPR000719 (Prot kinase), IPR017441 (Protein kinase ATP), IPR008271 (Ser/Thr kinase), IPR039192 (GSK3) | 典型 Ser/Thr 蛋白激酶 |
| Pfam | PF00069 (Pkinase) | Protein kinase domain |

经典 Ser/Thr 激酶，Wnt 信号核心组分。通过磷酸化 beta-catenin, APC, AXIN 等调控 Wnt 通路。磷酸化多种转录因子（MYC, JUN 等）和 mTORC2 组分 (RICTOR)。激酶活性直接参与基因表达调控。

#### 3.6 PPI 网络（三源综合）

**STRING 预测互作 (TOP 15, combined score >0.8)**:
| Partner | Score | Experimental | 功能类别 |
|---|---|---|---|
| AXIN1 | 0.999 | 0.936 | Wnt destruction complex |
| APC | 0.997 | 0.234 | Wnt destruction complex |
| CTNNB1 | 0.996 | 0.867 | Wnt effector |
| AKT1 | 0.993 | 0.895 | Upstream kinase |
| CSNK1A1 | 0.991 | 0.071 | Wnt destruction complex |
| GSK3B | 0.980 | 0.783 | Paralog kinase |
| AXIN2 | 0.962 | 0.837 | Wnt destruction complex |
| AKT3 | 0.937 | 0.125 | Upstream kinase |
| AKT2 | 0.937 | 0.125 | Upstream kinase |
| APP | 0.927 | 0.602 | Alzheimer substrate |
| MAPT | 0.911 | 0.749 | Tau phosphorylation |

**实验验证互作 (IntAct, 精选)**:
| Partner | 方法 | PMID | 功能类别 |
|---|---|---|---|
| YWHAG | anti bait coIP | 17353931 | 14-3-3 scaffold |
| GSKIP | two hybrid pooling | 20368287 | GSK3 inhibitor |
| NBR1 | pull down | 20368287 | Autophagy receptor |
| DEAF1 | protein kinase assay | 20368287 | Transcription factor |
| SPICE1 | pull down | 20368287 | Centrosome |
| MAP3K11 | pull down | 20368287 | MAPK signaling |
| ARHGEF11 | pull down | 20368287 | RhoGEF |
| VTA1 | pull down | 20368287 | Vesicle trafficking |

**UniProt 记录互作**: APP, AXIN1 (6exp), AXIN2 (4exp), BRAF (6exp), DEAF1, FRAT1 (5exp), GSKIP (6exp), HTT (6exp), LRP6, MAPT, NBR1 (7exp), YWHAE, YWHAG (5exp), ZDHHC17

Wnt 信号网络核心节点：AXIN1/APC/CTNNB1/GSK3B 构成 destruction complex。AKT1 为上游抑制性激酶。多个实验验证互作覆盖 Wnt, Alzheimer, autophagy 通路。

#### 3.7 多库互证
| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 定位 | HPA / GO | Nucleoplasm + Cytosol / nucleus+cytoplasm+cytosol | 一致 |
| PPI | STRING / IntAct / UniProt | AXIN1, GSKIP, NBR1, DEAF1, YWHAG 多源重叠 | 高度互证 |
| 结构 | AlphaFold + PDB | pLDDT=78.9 + 2 PDB entries | 实验+预测双重支持 |

**互证加分明细**: +2 (定位多源一致 + PPI 三源高度重叠 + 结构双重支持)
**总计**: +2 / max +3

### 4. 总体评价

**推荐等级**: 3星 (63.4/100)

GSK3A 是 Wnt 信号核心激酶，PPI 网络极其丰富（AXIN1/CTNNB1/GSK3B/AKT1），结构资源充足（PDB + pLDDT=78.9）。HPA Approved 级别 Nucleoplasm 定位。主要限制是研究量 (PM=80) 导致新颖性评分 4/10，且 GSK3B 主导该领域研究。GSK3A 特异性功能仍有探索空间。

**核心优势**:
1. 强核定位: HPA Approved Nucleoplasm（主定位）
2. Massive PPI 网络: Wnt destruction complex 核心
3. 结构资源丰富: PDB + AlphaFold pLDDT=78.9
4. 明确调控功能: 磷酸化多种转录因子

**风险/不确定性**:
1. PubMed=80，新颖性有限
2. GSK3B 研究占主导，GSK3A 特异性需区分
3. 核-质穿梭机制使实验设计复杂

**下一步建议**:
- GSK3A 特异性功能分析（区分 GSK3B）
- ChIP-seq 鉴定 GSK3A 下游靶基因
- 条件性核定位信号突变体

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P49840
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P49840
- PDB: 7SXF, 7SXG
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22GSK3A%22%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000105723-GSK3A

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GSK3A/IF_images/2064_E12_1_blue_red_green.jpg]]

![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/GSK3A/IF_images/2064_E12_3_blue_red_green.jpg]]

HPA IF 图像已本地嵌入。



**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P49840-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
