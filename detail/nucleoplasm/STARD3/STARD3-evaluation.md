---
type: protein-evaluation
gene: "STARD3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## STARD3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STARD3 / CAB1, MLN64 |
| 蛋白名称 | StAR-related lipid transfer protein 3 |
| 蛋白大小 | 445 aa / 50.5 kDa |
| UniProt ID | Q14849 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Vesicles; 额外: Endoplasmic reticulum; UniProt: Late endosome membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 445 aa / 50.5 kDa |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=96 篇 (≤100→2) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=81.4; PDB: 1EM2, 5I9J, 6TQR, 6TQU |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR019498, IPR000799, IPR051869, IPR029867, IPR023 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.0/180** | |
| **归一化总分** | | | **57.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles; 额外: Endoplasmic reticulum | Approved |
| UniProt | Late endosome membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum-endosome membrane contact site (GO:0140284)
- endosome (GO:0005768)
- late endosome membrane (GO:0031902)
- lysosomal membrane (GO:0005765)
- mitochondrion (GO:0005739)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 96 |
| PubMed broad count | 169 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CAB1, MLN64 |

**关键文献**:
1. Mitochondrial cholesterol import.. *Biochimica et biophysica acta. Molecular and cell biology of lipids*. PMID: 27565112
2. Regulatory roles of external cholesterol in human airway epithelial mitochondrial function through STARD3 signalling.. *Clinical and translational medicine*. PMID: 35678098
3. Touché! STARD3 and STARD3NL tether the ER to endosomes.. *Biochemical Society transactions*. PMID: 27068960
4. Blockade of STARD3-mediated cholesterol transport alleviates diabetes-induced podocyte injury by reducing mitochondrial cholesterol accumulation.. *Life sciences*. PMID: 38754814
5. The lysosomal lipid transporter LIMP-2 is part of lysosome-ER STARD3-VAPB-dependent contact sites.. *Journal of cell science*. PMID: 39370902

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.4 |
| 高置信度残基 (pLDDT>90) 占比 | 54.2% |
| 置信残基 (pLDDT 70-90) 占比 | 24.3% |
| 中等置信 (pLDDT 50-70) 占比 | 5.2% |
| 低置信 (pLDDT<50) 占比 | 16.4% |
| 有序区域 (pLDDT>70) 占比 | 78.5% |
| 可用 PDB 条目 | 1EM2, 5I9J, 6TQR, 6TQU |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1EM2, 5I9J, 6TQR, 6TQU）+ AlphaFold高质量预测（pLDDT=81.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019498, IPR000799, IPR051869, IPR029867, IPR023393; Pfam: PF10457, PF01852 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| VAPA | 0.990 | 0.833 | — |
| MOSPD2 | 0.980 | 0.926 | — |
| STARD3NL | 0.942 | 0.000 | — |
| PGAP3 | 0.942 | 0.000 | — |
| VAPB | 0.940 | 0.710 | — |
| PCTP | 0.938 | 0.000 | — |
| NPC2 | 0.925 | 0.000 | — |
| ZFYVE27 | 0.895 | 0.000 | — |
| NPC1 | 0.863 | 0.000 | — |
| GRB7 | 0.858 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CBARP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RNF170 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MME | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ERGIC3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CLEC2D | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AQP6 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TSPYL6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SPACA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SLC15A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| MANSC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.4 + PDB: 1EM2, 5I9J, 6TQR, 6TQU | pLDDT=81.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Late endosome membrane / Nucleoplasm, Vesicles; 额外: Endoplasmic reticulum | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. STARD3 — StAR-related lipid transfer protein 3，研究基础较多，新颖性有限。
2. 蛋白大小445 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 96 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q14849
- Protein Atlas: https://www.proteinatlas.org/ENSG00000131748-STARD3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STARD3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q14849
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (uncertain)。来源: https://www.proteinatlas.org/ENSG00000131748-STARD3/subcellular

![](https://images.proteinatlas.org/24307/1864_H4_15_cr5b7290693a466_red_green.jpg)
![](https://images.proteinatlas.org/24307/1864_H4_19_cr5b7290693a775_red_green.jpg)
![](https://images.proteinatlas.org/24307/1898_H5_4_cr5ba8a4807f7ff_red_green.jpg)
![](https://images.proteinatlas.org/24307/1898_H5_8_cr5ba8a48080536_red_green.jpg)
![](https://images.proteinatlas.org/73948/1559_A10_2_red_green.jpg)
![](https://images.proteinatlas.org/73948/1559_A10_6_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q14849-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
