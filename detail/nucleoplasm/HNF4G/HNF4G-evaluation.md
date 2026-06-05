---
type: protein-evaluation
gene: "HNF4G"
date: 2026-06-01
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## HNF4G 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | HNF4G / NR2A2 / Hepatocyte nuclear factor 4-gamma |
| 蛋白全名 | Hepatocyte nuclear factor 4-gamma |
| 蛋白大小 | 408 aa / 45.9 kDa |
| UniProt ID | Q14541 |

**HPA IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HNF4G/IF_images/A-549_1.jpg|A-549]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HNF4G/IF_images/PC-3_1.jpg|PC-3]]

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 7/10 | x4 | 28.0 | HPA Enhanced: Nucleoplasm (main) + Cytosol/Mitotic spindle/Cytokinetic bridge (additional); UniProt: Nucleus; GO: nucleoplasm (IDA)+chromatin (ISA) |
| 蛋白大小 | 8/10 | x1 | 8.0 | 408 aa, 45.9 kDa, 核受体超家族 |
| 研究新颖性 | 6/10 | x5 | 30.0 | PubMed strict=52 |
| 三维结构 | 8/10 | x3 | 24.0 | PDB: 1LV2 (2.70A, DBD+LBD); AlphaFold pLDDT=80.5, pct>90=62.5% |
| 调控结构域 | 8/10 | x2 | 16.0 | Nuclear receptor: zinc finger DBD (IPR001628) + ligand-binding domain (IPR000536); transcription factor |
| PPI 网络 | 5/10 | x3 | 15.0 | IntAct: HMGN2 (cross-linking), ZNF629/Y2H; STRING: HNF1A (0.943), FOXA2, NCOR1/NCOR2, MED1 |
| **加权总分** | | | **121/180**** | |
| 互证加分 | | | +1.0 | HPA Enhanced+UniProt+GO 定位一致; PDB+AlphaFold 结构互证; STRING+IntAct PPI 部分重叠 |
| **归一化总分 (÷1.83)** | | | **66.1/100**** | |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| HPA | Nucleoplasm (main), Cytosol (additional), Cytokinetic bridge (additional), Mitotic spindle (additional) | Enhanced |
| UniProt | Nucleus (ECO:0000255) | Predicted |
| GO-CC | chromatin (ISA), cytosol (IDA), intercellular bridge (IDA), mitotic spindle (IDA), nucleoplasm (IDA) | - |

**结论**: HPA Enhanced 级别（最高可靠性）Nucleoplasm 主定位。UniProt/GO 一致支持。HNF4G 是核受体超家族成员，核定位明确。

#### 3.2 蛋白大小评估
408 aa, 45.9 kDa。核受体，含 zinc finger DBD + ligand-binding domain。适合重组表达。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed strict (Title/Abstract) | 52 |
| PubMed broad | 100 |
| 新颖性级别 | 有一定研究 |

PubMed 52 篇。HNF4G 主要在 kidney organoid gene regulatory network、pancreatic cancer subtype switching、intestinal stem cell 方向有研究。HNF4A（更知名 paralog）主导该领域，HNF4G 特异性研究仍存 niche 空间。

**关键文献**:
1. Rao SV et al. (2025). "Transcription factor switching drives subtype-specific pancreatic cancer." *Nat Genet*. PMID: 41168397
2. Yoshimura Y et al. (2023). "Elucidating the Proximal Tubule HNF4A Gene Regulatory Network in Human Kidney Organoids." *J Am Soc Nephrol*. PMID: 37488681
3. Chen L et al. (2020). "HNF4 Regulates Fatty Acid Oxidation and Is Required for Renewal of Intestinal Stem Cells in Mice." *Gastroenterology*. PMID: 31759926
4. Suzuki T et al. (2023). "Beta-Catenin Drives Butyrophilin-like Molecule Loss and gammadelta T-cell Exclusion in Colon Cancer." *Cancer Immunol Res*. PMID: 37309673
5. Galanakis V et al. (2026). "Transcriptomic and epigenetic mechanisms controlling cholangiocyte transdifferentiation into hepatocytes." *J Hepatol*. PMID: 41033615

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold | AF-Q14541-F1 v6 |
| 平均 pLDDT | 80.5 |
| pLDDT >90 | 62.5% |
| pLDDT 70-90 | 10.5% |
| pLDDT 50-70 | 6.4% |
| pLDDT <50 | 20.6% |
| PDB | 1LV2 (2.70A, aa103-328, DBD+LBD) |

**AlphaFold PAE**:

高质量结构：pLDDT=80.5，62.5% >90。1LV2 PDB 结构覆盖 DNA-binding domain (zinc fingers) + ligand-binding domain。N 端 A/B domain 和 C 端 F domain 为无序区域。

#### 3.5 结构域分析
| 来源 | 结构域 | 备注 |
|---|---|---|
| InterPro | IPR049636/049635 (HNF4), IPR035500 (HNF4-like), IPR000536 (Nuclear hormone receptor LBD), IPR050274 (HNF4), IPR001723 (Nuclear hormone receptor), IPR001628 (Zinc finger nuclear receptor), IPR013088 (Zinc finger NHR/GATA) | 典型核受体结构: DBD+LBD |
| Pfam | PF00104 (Hormone_recep LBD), PF00105 (zf-C4 zinc finger DBD) | DNA-binding + ligand-binding |
| PDB | 1LV2 | 实验结构覆盖 DBD+LBD |

经典核受体超家族成员。Zinc finger DNA-binding domain (PF00105) 识别 HNF4 response elements。Ligand-binding domain (PF00104) 调控转录活性。HNF4A paralog。

#### 3.6 PPI 网络（三源综合）

**实验验证互作 (IntAct)**:
| Partner | 方法 | PMID | 功能类别 |
|---|---|---|---|
| HMGN2 | cross-linking study | 30021884 | Nucleosome binding |
| ZNF629 | validated two hybrid | 32296183 | Zinc finger TF |
| HLF | two hybrid array | 20211142 | bZIP TF |
| Nr0b2 | two hybrid array | 20211142 | Nuclear receptor |
| Ncoa3 | two hybrid array | 20211142 | Nuclear receptor coactivator |
| Nkx2-1 | two hybrid array | 20211142 | Homeobox TF |
| Dlx5 | two hybrid array | 20211142 | Homeobox TF |
| Emx1 | two hybrid array | 20211142 | Homeobox TF |
| Tlx3 | two hybrid array | 20211142 | Homeobox TF |

**STRING 预测互作 (combined score >0.4)**:
| Partner | Score | 证据类型 | 功能类别 |
|---|---|---|---|
| HNF1A | 0.943 | experimental=0.085, database=0.750 | Hepatocyte TF |
| FOXA2 | 0.777 | experimental=0.070 | Pioneer TF |
| PFKFB1 | 0.766 | textmining | Glycolysis |
| ONECUT1 | 0.680 | experimental=0.062 | Hepatocyte TF |
| NCOR1 | 0.557 | database=0.500 | Corepressor |
| NCOR2 | 0.535 | database=0.500 | Corepressor |
| FOXA1 | 0.556 | experimental=0.070 | Pioneer TF |
| MED1 | 0.506 | database=0.500 | Mediator complex |
| FOXA3 | 0.561 | experimental=0.070 | Pioneer TF |
| FOXM1 | 0.558 | experimental=0.048 | Forkhead TF |

**UniProt 记录互作**: ZNF629 (3exp)

HNF1A/FOXA2/ONECUT1 构成肝细胞转录调控网络，NCOR1/NCOR2 为核心抑制因子。HNF4G 作为 HNF4 家族成员参与 hepatocyte/intestinal 分化调控。PPI 以预测和数据库为主，实验互作较少但功能方向明确。

#### 3.7 多库互证
| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 定位 | HPA / UniProt / GO | Nucleoplasm / Nucleus / nucleoplasm+chromatin | 三源一致 (HPA Enhanced) |
| PPI | STRING / IntAct | ZNF629 多源确认 | 有限互证 |
| 结构 | AlphaFold + PDB | pLDDT=80.5 + 1LV2 | 实验+预测双重支持 |

**互证加分明细**: +1 (定位三源一致 + 结构双重支持)
**总计**: +1 / max +3

### 4. 总体评价

**推荐等级**: 3星 (66.7/100)

HNF4G 是经典核受体转录因子，HPA Enhanced 级别最高可信度核定位。结构质量好 (pLDDT=80.5 + PDB 1LV2)。定位于肝细胞/肠道/肾脏分化调控网络。PubMed=52，有一定研究但 niche 空间存在（HNF4A 主导该领域）。作为已知 TF，调控功能明确但新颖性中等。

**核心优势**:
1. HPA Enhanced 最高可信度核定位
2. 经典核受体：zinc finger DBD + LBD，调控功能明确
3. 结构质量好: pLDDT=80.5 + PDB 1LV2
4. 肝细胞/肠道/肾脏 TF 调控网络定位清晰

**风险/不确定性**:
1. PubMed=52，新颖性中等
2. HNF4A 主导研究领域，HNF4G 特异性需区分
3. PPI 以预测和数据库为主，实验互作较少

**下一步建议**:
- HNF4G 特异性靶基因鉴定（区分 HNF4A）
- ChIP-seq 在全基因组水平鉴定 HNF4G 结合位点
- 条件性敲除表型分析

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14541
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14541
- PDB: 1LV2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22HNF4G%22%5BTitle/Abstract%5D
- HPA: https://www.proteinatlas.org/ENSG00000164749-HNF4G

HPA IF 图像已本地嵌入。



**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14541-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
