---
type: protein-evaluation
gene: "HEATR5B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HEATR5B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HEATR5B / KIAA1414, p200, p200a |
| 蛋白名称 | HEAT repeat-containing protein 5B |
| 蛋白大小 | 2071 aa / 224.3 kDa |
| UniProt ID | Q9P2D3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus, Vesicles; 额外: Nucleoplasm, Cytosol; UniProt: Cytoplasm, perinuclear region; Cytoplasmic vesicle, clathrin |
| 蛋白大小 | 2/10 | ×1 | 2 | 2071 aa / 224.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=5 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=81.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR040108, IPR046837; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **127.5/180** | |
| **归一化总分** | | | **70.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Vesicles; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm, perinuclear region; Cytoplasmic vesicle, clathrin-coated vesicle | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- clathrin-coated vesicle (GO:0030136)
- cytosol (GO:0005829)
- endocytic vesicle (GO:0030139)
- Golgi apparatus (GO:0005794)
- membrane (GO:0016020)
- nucleoplasm (GO:0005654)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 5 |
| PubMed broad count | 7 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1414, p200, p200a |

**关键文献**:
1. A novel protein encoded by ZCRB1-induced circHEATR5B suppresses aerobic glycolysis of GBM through phosphorylation of JMJD5.. *Journal of experimental & clinical cancer research : CR*. PMID: 35538499
2. Searching for candidate genes in familial BRCAX mutation carriers with prostate cancer.. *Urologic oncology*. PMID: 26585945
3. Biallelic hypomorphic mutations in HEATR5B, encoding HEAT repeat-containing protein 5B, in a neurological syndrome with pontocerebellar hypoplasia.. *European journal of human genetics : EJHG*. PMID: 33824466
4. A novel HEAT repeat protein 5B anaplastic lymphoma kinase fusion in lung adenocarcinoma confers sensitivity to ensartinib.. *Anti-cancer drugs*. PMID: 42003316
5. HEATR5B associates with dynein-dynactin and promotes motility of AP1-bound endosomal membranes.. *The EMBO journal*. PMID: 37872872

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.2 |
| 高置信度残基 (pLDDT>90) 占比 | 33.9% |
| 置信残基 (pLDDT 70-90) 占比 | 50.9% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 8.1% |
| 有序区域 (pLDDT>70) 占比 | 84.8% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=81.2，有序区 84.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR040108, IPR046837; Pfam: PF25468, PF20210 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| AP1M2 | 0.768 | 0.765 | — |
| AP1S2 | 0.670 | 0.667 | — |
| TRAPPC11 | 0.643 | 0.000 | — |
| AP1G1 | 0.598 | 0.500 | — |
| AFTPH | 0.592 | 0.326 | — |
| TTC17 | 0.516 | 0.000 | — |
| SYNRG | 0.499 | 0.300 | — |
| AP1S3 | 0.492 | 0.492 | — |
| MON2 | 0.484 | 0.000 | — |
| SLC22A18AS | 0.473 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CALM1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16512683|imex:IM-19867 |
| ENSP00000233099.5 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| DLG1 | psi-mi:"MI:0900"(p8 filamentous phage display) | imex:IM-26482|pubmed:30126976 |
| SCRIB | psi-mi:"MI:0900"(p8 filamentous phage display) | imex:IM-26482|pubmed:30126976 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| PTPN3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:28330616|imex:IM-25671 |
| VAPA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| VAPB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AURKA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AP1S2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.2 + PDB: 无 | pLDDT=81.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region; Cytoplasmic vesicle / Golgi apparatus, Vesicles; 额外: Nucleoplasm, Cytoso | 一致 |
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
1. HEATR5B — HEAT repeat-containing protein 5B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小2071 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 5 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2D3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000008869-HEATR5B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HEATR5B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2D3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
