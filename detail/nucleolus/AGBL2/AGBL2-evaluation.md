---
type: protein-evaluation
gene: "AGBL2"
date: 2026-05-29
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## AGBL2 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | AGBL2 / Cytosolic carboxypeptidase 2 / CCP2 |
| 蛋白大小 | 902 aa / 104.2 kDa |
| UniProt ID | Q5U5Z8 |
| 评估日期 | 2026-05-29 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA IF Approved: Nucleoli (main) + Cytosol + Basal body |
| 蛋白大小 | 8/10 | ×1 | 8 | 902 aa (800-1200 aa区间) |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed 21篇 (21-50区间) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold pLDDT 71.69 (mean), 60.7% >70, 无PDB |
| 调控结构域 | 7/10 | ×2 | 14 | Peptidase M14 (carboxypeptidase), baseline |
| PPI 网络 | 2/10 | ×3 | 6 | IntAct 9条, GO-CC centriole/cilium/cytoplasm |
| 互证加分 | — | max +3 | +0.5 | Protein Atlas nucleoli Approved + AlphaFold 中等质量 |
| **原始总分** |  |  | **121.5/183** |  |
| **归一化总分** |  |  | **66.4/100** |  |

### 3. 详细分析

#### 3.1 核定位证据
| 来源 | 定位 | 可信度 |
|---|---|---|
| Protein Atlas (IF) | Nucleoli (main, approved) + Cytosol + Basal body + Flagellar centriole | Supported |
| UniProt | Cytoplasm, Cytosol, Centrosome, Centriole, Cilium basal body | — |

**IF 图像**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/AGBL2/IF_images/ASC52telo_1.jpg|ASC52telo]]
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/AGBL2/IF_images/hTERT-RPE1_1.jpg|hTERT-RPE1]]

**结论**: 核仁 + 胞质 + 基体多定位。HPA Supported 可靠性，ASC52telo 和 hTERT-RPE1 均显示核仁信号。核仁定位为 Approved 主要定位之一。UniProt 未标注核定位，但 HPA IF 提供实验证据。

#### 3.2 蛋白大小评估
**评价**: 902 aa, 104.2 kDa。中等偏大 (800-1200 aa 区间)，进行生化实验有一定挑战性，但仍可进行体外研究。

#### 3.3 研究现状
| 指标 | 数值 |
|---|---|
| PubMed 总数 | 21 |
| 最早发表年份 | 2015 |
| Chromatin/epigenetics 比例 | 极低 |

**主要研究方向**:
- alpha-tubulin detyrosination (微管去酪氨酸化)
- 肾细胞癌增殖与迁移
- 乳腺癌 (AGBL2 表达与乳腺癌预后)
- 精子发生 (testis-enriched genes)
- 骨质疏松 (CNV 分析)

**关键文献**:
1. Liu W et al. (2024). "AGBL2 promotes renal cell carcinoma cells proliferation and migration via alpha-tubulin detyrosination". *Heliyon*. PMID: 39315218
2. Zhang H et al. (2025). "Correction to: Clinical implications of AGBL2 expression and its inhibitor latexin in breast cancer". *World J Surg Oncol*. PMID: 40369660
3. Lovsin N et al. (2023). "Copy Number Variation and Osteoporosis". *Curr Osteoporos Rep*. PMID: 36795294
4. Zhou J et al. (2026). "The Effect and Its Mechanism of a Novel Disintegrin GbvIV4 From Gloydius brevicaudus Venom on Inhibition Metastasis of Melanoma Cells". *J Appl Toxicol*. PMID: 41292126
5. Fu H et al. (2025). "CRISPR/Cas9-mediated genome editing reveals six testis-enriched genes dispensable for male fertility in mice". *J Biomed Res*. PMID: 41194443

**评价**: 21 篇，刚好进入 21-50 区间 (新颖性 8)。研究主要聚焦于 de-tyrosinase 酶活和癌症关联。核仁定位的功能角色完全未研究，存在全新探索机会。

#### 3.4 三维结构分析
| 指标 | 数值 |
|---|---|
| AlphaFold 平均 pLDDT | 71.69 |
| pLDDT >90 占比 | 48.3% |
| pLDDT 70-90 占比 | 12.4% |
| pLDDT <50 占比 | 32.7% |
| 可用 PDB 条目 | 0 |

**PAE 图**:
![[Projects/TEreg-finding/protein-interested/detail/nucleolus/AGBL2/AGBL2-PAE.png]]

**评价**: AlphaFold 中等质量预测 (mean pLDDT 71.69)，60.7% 残基 >70。Peptidase M14 催化域 (396-666) 预计为高质量折叠 (类似 carboxypeptidase 家族)。C 端 (796-879) 存在显著无序区域。无 PDB 实验结构。

#### 3.5 结构域分析
| 来源 | 结构域 |
|---|---|
| UniProt InterPro | Cytosolic_carboxypeptidase, Peptidase M14, Pepdidase_M14_N |
| Pfam | Pepdidase_M14_N, Peptidase_M14 |
| PROSITE | PEPTIDASE_M14 |

**染色质调控潜力分析**: Peptidase M14 是锌离子依赖性羧肽酶结构域，催化 alpha-tubulin 去酪氨酸化。与染色质/DNA 无已知关联。但 AGBL2 的核仁定位提示可能存在独立的核仁功能（如 rRNA 加工相关蛋白的去酪氨酸化）。baseline 评分。

#### 3.6 PPI 网络

**实验验证互作** (IntAct):

| Partner | 方法 | 功能类别 | 调控相关？ |
|---|---|---|---|
| 微管/纤毛相关蛋白 | Two-hybrid/CLASH | 细胞骨架 | 否 |

**STRING 预测互作**: API 不可用。

**已知复合体成员** (GO Cellular Component):
- Centriole
- Ciliary basal body
- Cytoplasm
- Cytosol
- Microtubule cytoskeleton

**PPI 互证分析**:
- IntAct 实验验证: 9 条
- GO-CC: 均为胞质/细胞骨架组分
- 核仁相关 partner: 0

**评价**: PPI 数据稀少，主要反映细胞骨架功能。核仁功能的 PPI 完全未知，在新颖蛋白中属正常。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|---|---|---|---|
| 定位 | Protein Atlas IF / UniProt | Nucleoli + Cytosol vs Cytoplasm/Centrosome | 部分一致 |
| 结构域 | UniProt / InterPro / Pfam / PROSITE | Peptidase M14 多库确认 | 一致 |

**互证加分明细**:
- Peptidase M14 多库确认: +0.5
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: (2/5)

**核心优势**:
1. 核仁定位 Approved (HPA IF)
2. Peptidase M14 酶活为可检测的生化活性
3. 大小适中 (902 aa)

**风险/不确定性**:
1. 主要为胞质羧肽酶，核仁功能完全未知
2. PPI 稀少，无可关联核仁功能的互作
3. UniProt 无核定位注释
4. 核仁定位可能与细胞周期相关（需独立验证）

**下一步建议**:
- [ ] 确认 AGBL2 在核仁中的底物
- [ ] 探索是否有核仁蛋白作为去酪氨酸化底物

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5U5Z8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165923-AGBL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22AGBL2%22
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5U5Z8


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。

![[AGBL2-PAE.png]]

PAE 图像已获取。结构判断基于 AlphaFold pLDDT 统计。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleolus/AGBL2/AGBL2-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q5U5Z8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 396..666; /note="Peptidase M14"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01379" |
| InterPro | IPR050821;IPR040626;IPR000834; |
| Pfam | PF18027;PF00246; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000165923-AGBL2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| NUDT5 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
