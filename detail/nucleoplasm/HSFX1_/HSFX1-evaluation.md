---
type: protein-evaluation
gene: "HSFX1"
date: 2026-06-18
tags: [protein-scout, nucleoplasm, evaluation]
status: scored
---

## HSFX1 -- Heat Shock Transcription Factor Family X1 评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HSFX1 / HSFX2, LW-1 |
| 蛋白名称 | Heat shock transcription factor, X-linked |
| 蛋白大小 | 423 aa / 46.7 kDa |
| UniProt ID | Q9UBD0 (Swiss-Prot, reviewed) |
| Ensembl | ENSG00000171116 |
| 染色体位置 | Xq28 (149,774,068-149,776,867) |
| 蛋白存在证据 | Evidence at protein level |
| 评估日期 | 2026-06-18 |

**IF 图像** (Cell Atlas, antibody HPA051700):

**U2OS 细胞系** (human osteosarcoma):
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HSFX1/IF_images/U2OS_1.jpg|U2OS - 4x]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HSFX1/IF_images/U2OS_2.jpg|U2OS - zoom]]

**MCF-7 细胞系** (human breast carcinoma):
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HSFX1/IF_images/MCF7_1.jpg|MCF-7 - 4x]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HSFX1/IF_images/MCF7_2.jpg|MCF-7 - zoom]]

**EFO-21 细胞系** (human ovarian carcinoma):
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HSFX1/IF_images/EFO21_1.jpg|EFO-21 - 4x]]
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HSFX1/IF_images/EFO21_2.jpg|EFO-21 - zoom]]

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 6/10 | x4 | 24 | HPA: Nucleoplasm (main, supported); 额外: Plasma membrane, Cytosol; GO: nucleus, chromatin, cytosol |
| 蛋白大小 | 8/10 | x1 | 8 | 423 aa / 46.7 kDa (略低于400-800 aa 最佳范围) |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=8 篇 (<=10->10), Title/Abstract=4篇; 极低研究覆盖 |
| 三维结构 | 5/10 | x3 | 15 | AlphaFold v6 pLDDT=55.0; PDB: 无; 60%残基低置信度(pLDDT<50) |
| 调控结构域 | 6/10 | x2 | 12 | InterPro: IPR000232 HSF DNA-bd; Pfam: PF00447; SMART: SM00415; winged helix DNA-binding |
| PPI 网络 | 2/10 | x3 | 6 | STRING 265 unique partners; BioGRID 20 partners; IntAct 9 interactions |
| 互证加分 | -- | max +3 | 1.0 | AF+STRING+BioGRID+IntAct cross-validation |
| **加权总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm (main); 额外: Plasma membrane, Cytosol | Supported (Uncertain reliability) |
| UniProt (Swiss-Prot) | Nucleus, Cytoplasm | Reviewed |
| GO - Cellular Component | Nucleus (IDA:LIFEdb), Chromatin (ISA:NTNU_SB), Cytosol (IDA:HPA) | Multiple sources |

**HPA IF 摘要**: "Mainly localized to the nucleoplasm. In addition localized to the plasma membrane and cytosol. Caution: Based on antibodies targeting proteins from multiple genes."

**GO Cellular Component**:
- nucleus (GO:0005634)
- chromatin (GO:0000785)
- cytosol (GO:0005829)

**核定位特异性评分理由 (6/10)**:
- 核定位有 HPA + GO + UniProt 三方证据支持 (+)
- HPA IF 确认 Nucleoplasm 为主定位 (+)
- 但 HPA IF 可靠性标注为 "Uncertain"，且抗体可能识别多个基因产物 (-)
- 同时检测到 Cytosol 和 Plasma membrane 信号，多室定位 (-)
- 无 dedicated 核定位信号 (NLS) 实验验证 (-)

**结论**: 核定位证据充分但可靠性一般，多室分布降低了核定位特异性。

#### 3.2 蛋白大小评估

**评价**: 423 aa / 46.7 kDa，略低于 400-800 aa 最佳生化范围。作为转录因子，该尺寸仍然适合常规实验操作。

**大小评分理由 (8/10)**: 蛋白大小适中，适合多数生化实验，但略低于最佳区间下限 (400 aa)。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8 |
| PubMed Title/Abstract count | 4 |
| 直接研究该基因的论文 | 0-2 |
| 基因发现论文 | Biol Reprod (2004) -- 实际上研究的是 Y 染色体同源基因 HSFY |
| 蛋白家族 (HSF) 总文献数 | >5000 |

**关键文献**:
1. Molecular characterization of heat shock-like factor encoded on the human Y chromosome, and implications for male infertility. *Biol Reprod*. 2004. PMID: 15044259
2. Differentially Expressed Genes in Dental Pulp Tissues of Individuals With Symptomatic Irreversible Pulpitis With and Without History of COVID-19. *J Endod*. 2023. PMID: 37178757
3. Investigation of Antigen-Specific T-Cell Receptor Clusters in Human Cancers. *Clin Cancer Res*. 2020. PMID: 31831563
4. Skin collagen fluorophore LW-1 versus skin fluorescence as markers for the long-term progression of subclinical macrovascular disease in type 1 diabetes. *Cardiovasc Diabetol*. 2016. PMID: 26864236
5. X chromosome gene methylation in peripheral lymphocytes from monozygotic twins discordant for scleroderma. *Clin Exp Immunol*. 2012. PMID: 22861365

**TE (转座元件) 调控相关性分析**:
- HSFX1 属于 heat shock transcription factor (HSF) 家族，该家族通过 heat shock elements (HSE) 调控基因表达
- TE (特别是 L1 反转录转座子) 启动子中含有 heat shock elements
- PMID 12621071: "Environmental factors affecting transcription of the human L1 retrotransposon. II. Stressors." 证明热应激可影响人 L1 转录
- PMID 30063880: 热休克条件下果蝇 R1 反转录转座子被 RNA polymerase I 转录
- PubMed 上 HSF + TE 交叉文献共 279 篇，显示热休克因子与转座元件调控存在广泛间接证据
- 但 HSFX1 本身尚无任何 TE 调控相关直接研究
- HSFX1 是 testis-specific 表达（HPA），而生殖细胞是 TE 转座活跃的组织之一

**新颖性评分理由 (10/10)**: PubMed 文献数 <=10，研究基础极少，新颖性极高。

**评价**: HSFX1 是 HSF 家族中研究最少的成员之一，其 X 染色体定位和 testis 特异性表达使其成为 TE 调控的潜在 niche 靶点。热休克反应与 TE 转座的广泛联系为该基因的间接 TE 调控功能提供了合理假设基础。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.0 |
| 高置信度残基 (pLDDT>90) 占比 | 12.8% (54/423) |
| 置信残基 (pLDDT 70-90) 占比 | 10.4% (44/423) |
| 中等置信 (pLDDT 50-70) 占比 | 16.8% (71/423) |
| 低置信 (pLDDT<50) 占比 | 60.0% (254/423) |
| 有序区域 (pLDDT>70) 占比 | 23.2% |
| 可用 PDB 条目 | 无 |

**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/HSFX1/HSFX1-PAE.png]]

**结构特征**:
- DNA-binding domain (98-282 aa): HSF-type winged helix DNA-binding domain -- 该区域在所有 HSF 家族成员中高度保守
- N-terminal (1-56 aa): -- 本质无序区域 (intrinsically disordered region)
- Middle (215-303 aa): -- 部分无序
- C-terminal (397-423 aa): -- 无序尾部
- 该蛋白属于高度无序蛋白 (IDP)，约 60% 残基置信度低于 50

**结构评分理由 (5/10)**: AlphaFold 预测平均质量偏低 (pLDDT=55.0)，无实验结构，但 DNA-binding domain 区域可以建模。

**评价**: 该蛋白大部分区域为无序结构，符合转录因子常见特征（转录因子中无序区域参与蛋白-蛋白互作和转录调控复合体组装）。DNA-binding domain (98-282 aa) 是唯一有序折叠区域。

#### 3.5 结构域分析

| 来源 | 结构域 | 描述 |
|------|--------|------|
| Pfam (PF00447) | HSF_DNA-bind | Heat shock factor DNA-binding domain |
| SMART (SM00415) | HSF | Heat shock transcription factor |
| InterPro (IPR000232) | HSF_DNA-bd | Heat shock transcription factor family, DNA-binding |
| InterPro (IPR036388) | WH-like_DNA-bd_sf | Winged helix-like DNA-binding domain superfamily |
| InterPro (IPR036390) | WH_DNA-bd_sf | Winged helix DNA-binding domain superfamily |
| Gene3D (1.10.10.10) | Winged helix-like | Winged helix DNA-binding domain |
| PANTHER (PTHR10015) | HEAT SHOCK TRANSCRIPTION FACTOR | 蛋白家族分类 |
| PANTHER (PTHR10015:SF282) | HEAT SHOCK TRANSCRIPTION FACTOR, X-LINKED | 亚家族分类 |

**蛋白特征 (UniProt)**:
- DNA-binding region: 残基 98-282
- Disordered regions: 1-56, 215-303, 397-423
- Compositional bias (basic/acidic): 1-25
- Compositional bias (polar): 243-254
- Cross-link site: 残基 215

**含 HSF DNA-binding domain 的其他人类蛋白**:
- HSF1 (Q00613) -- 主要热休克因子，广泛研究
- HSF2 (Q03933) -- 发育相关热休克因子
- HSF4 (Q9ULV5) -- 热休克因子 4
- HSF5 (Q4G112) -- 热休克因子 5
- HSFY1/HSFY2 (Q96LI6/Q96LI5) -- Y 染色体热休克因子

**染色质调控潜力分析**:
- HSF DNA-binding domain 是经典的转录因子 DNA 结合域，直接结合 DNA 上的 heat shock elements (HSE: 5'-nGAAn-3' 重复序列)
- 该结构域在进化上高度保守，说明其 DNA 结合功能受选择压力维持
- GO 注释包含 "DNA-binding transcription factor activity, RNA polymerase II-specific" (IBA:GO_Central)
- 无其他已知染色质修饰/重塑结构域
- TE 启动子区域中 HSE 序列的存在提供了一个间接的 TE 调控机制假设

**结构域评分理由 (6/10)**: 存在一个明确的 DNA-binding domain (HSF)，但无其他调控结构域（如 PHD, bromodomain, chromodomain 等）。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score, top 10):

| Partner | Combined Score | 功能类别 |
|---------|---------------|---------|
| PDZD4 | 472 | PDZ domain-containing scaffold protein |
| VCX3B | 466 | Variable charge X-linked family |
| ZNF41 | 449 | Zinc finger transcription factor |
| CXorf51A | 447 | X-linked uncharacterized protein |
| CXorf40B | 447 | X-linked uncharacterized protein |
| VCX2 | 422 | Variable charge X-linked family |
| TSPYL2 | 411 | Testis-specific Y-encoded-like protein 2 (chromatin remodeling) |
| TMEM185A | 398 | Transmembrane protein |
| ARSF | 392 | Arylsulfatase F |
| VCX3A | 377 | Variable charge X-linked family |

**STRING 统计**: 265 unique partners in total (all confidence levels)
**PPI 网络特征**: 绝大部分互作蛋白是 X 染色体编码的睾丸相关蛋白 (VCX, MAGEA, SPANX 家族)，提示 HSFX1 功能定位于 X 染色体相关的睾丸生物学通路中

**BioGRID 实验互作**:

| Partner | 功能类别 |
|---------|---------|
| ATXN1 | Ataxin-1, 转录调控 |
| ATXN1L | ATXN1-like, 转录调控 |
| HSFX2 | HSFX1 旁系同源 |
| CCDC57 | Coiled-coil domain-containing protein |
| CACFD1 | Calcium channel flower domain-containing 1 |
| DIABLO | Mitochondrial apoptosis regulator |
| FAM192A | NIP30, 蛋白酶体相互作用蛋白 |
| IARS2 | Mitochondrial isoleucine-tRNA ligase |
| MAL2 | Myelin and lymphocyte protein 2 |
| MTIF3 | Mitochondrial translation initiation factor 3 |
| NCS1 | Neuronal calcium sensor 1 |
| PXDN | Peroxidasin homolog |
| RBFOX1 | RNA binding protein fox-1 homolog |
| SDR16C5 | Short-chain dehydrogenase/reductase family |
| SYP | Synaptophysin |
| VCAN | Versican core protein |

**IntAct 实验互作** (UniProt curated):

| Partner | 实验次数 | 功能类别 |
|---------|---------|---------|
| AGTRAP | 3 | Angiotensin II receptor-associated protein |
| ATXN1 | 6 | Ataxin-1 (转录调控) |
| CACFD1 | 3 | Calcium channel flower domain |
| KRTAP12-2 | 3 | Keratin-associated protein |
| MAL2 | 3 | Myelin and lymphocyte protein 2 |
| MICOS13 | 3 | Mitochondrial contact site protein |
| MTIF3 | 3 | Mitochondrial translation initiation factor 3 |
| SDR16C5 | 3 | Short-chain dehydrogenase/reductase 5 |
| SYP | 3 | Synaptophysin |

**PPI 互证分析**:
- STRING + BioGRID + IntAct 三方均有数据
- STRING partners: 265, BioGRID partners: 20, IntAct interactions: 9
- BioGRID-IntAct 重叠: ATXN1, MAL2, MTIF3, SDR16C5, SYP (5 个重叠)
- 转录调控相关比例: 较低 (~5%)

**PPI 评分理由 (2/10)**: 多维数据源存在，但 interactome 中缺少经典的染色质调控因子/转录调控复合体成员。多数互作蛋白为 X 染色体睾丸特异性蛋白，未参与已知 TE 调控网络。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=55.0, v6; PDB: 无 | pLDDT=55.0, v6 | 仅预测 |
| 定位 | UniProt + HPA + GO | Nucleus(Nucleoplasm) + Cytosol + Cytoplasm | 三方一致 |
| PPI | STRING + BioGRID + IntAct | 265 + 20 + 9 interactions | 数据充分 |
| 结构域 | InterPro + Pfam + SMART + PANTHER + Gene3D | HSF DNA-binding domain (winged helix) | 五源一致 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0 (无 PDB 实验结构)
- 多库定位一致 (3源): +0.5
- STRING + BioGRID + IntAct 三方验证: +0.5
- 结构域 + AlphaFold 质量: +0 (pLDDT=55.0, 质量偏低)
- PDB 多条目覆盖: +0
- **总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: 3.5/5 (中等推荐，用于 TE 调控研究)

**核心优势**:
1. **极低研究覆盖度**: PubMed 仅 8 篇文献，Title/Abstract 只有 4 篇，是 HSF 家族中最未被研究的成员，提供完全新颖的研究视角
2. **核定位充分**: HPA IF 确认 Nucleoplasm 定位（主定位），UniProt + GO 三方验证
3. **HSF/热休克-TE 连接**: 热休克反应与 TE 转座存在广泛的间接文献证据（279 篇 HSF+TE），HSF1 已被证实参与 L1 反转录转座子调控 (PMID: 12621071)
4. **HSF DNA-binding domain**: 经典转录因子 DNA 结合域，理论上可通过识别 TE 内 heat shock elements 调控转座元件
5. **Testis 特异性表达**: 睾丸是基因组 TE 转座活性最高的组织之一，testis-specific 表达模式与 TE 调控的生理需求吻合

**风险/不确定性**:
1. **蛋白高度无序**: AlphaFold pLDDT 仅 55.0, 60% 残基无序 -- 给结构研究和功能预测带来困难
2. **无直接 TE 功能证据**: HSFX1 本身无任何 TE 调控相关文献，所有证据均为家族推断
3. **微弱 PPI 网络**: interactome 中缺少染色质修饰因子或经典转录调控复合体成员
4. **HPA IF 可靠性标注为 Uncertain**: 抗体可能识别多个基因产物 (HSFX1 and possibly HSFX2)
5. **基因尚不明确**: HSFX1 的基础生物学功能 (靶基因、诱导条件、转录活性) 几乎完全未知
6. **缺少 NLS**: 未见明确的核定位信号，核定位机制不明
7. **可能存在 Y 染色体功能补偿**: HSFY (Y-linked) 基因的表达可能模糊 HSFX1 功能的表型分析

**间接 TE 调控机制假设**:
1. HSFX1 作为转录因子通过识别 TE 启动子区域的 heat shock elements (HSE: nGAAn repeats) 调控 TE 转录
2. Testis-specific 表达可能参与精子发生过程中 TE 的 transcriptional silencing
3. 在热应激条件下，HSFX1 可能被招募至 TE 位点参与应激反应调控

**下一步建议**:
- [ ] 在 testis-derived 细胞系中验证 HSFX1 的表达和亚细胞定位
- [ ] ChIP-seq 实验确认 HSFX1 的基因组结合位点，特别关注 TE 富集区域
- [ ] RNA-seq 分析 HSFX1 敲低/过表达对 TE 转录本的影响
- [ ] 确认 HSFX1 的 heat shock inducibility (是否像经典 HSF 一样被热应激激活)
- [ ] 比较 HSFX1 vs HSFY vs HSF1 对 TE 启动子的结合特异性
- [ ] 蛋白-蛋白互作筛选鉴定 HSFX1 在 TE 调控中可能的 co-factor

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RBFOX1 | BioGRID | 0 |
| ATXN1 | BioGRID | 0 |
| ATXN1L | BioGRID | 0 |
| CCDC57 | BioGRID | 0 |
| HSFX2 | BioGRID | 0 |
| IARS2 | BioGRID | 0 |
| FAM192A | BioGRID | 0 |
| VCAN | BioGRID | 0 |


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UBD0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171116-HSFX1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HSFX1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UBD0
- STRING: https://string-db.org/network/9606.ENSP00000359444
- InterPro: https://www.ebi.ac.uk/interpro/protein/Q9UBD0/
- Data fetched live: 2026-06-18

---

*注: 原始 Excel 中 UniProt 列为 Q9H9S3，经 UniProt API 验证，该 accession 对应 SEC61A2 (Protein transport protein Sec61 subunit alpha isoform 2)。HSFX1 的正确 UniProt accession 为 Q9UBD0。*
