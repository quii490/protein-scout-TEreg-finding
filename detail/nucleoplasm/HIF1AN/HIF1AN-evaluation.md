---
type: protein-evaluation
gene: "HIF1AN"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## HIF1AN 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | HIF1AN / FIH1 |
| 蛋白名称 | Hypoxia-inducible factor 1-alpha inhibitor |
| 蛋白大小 | 349 aa / 40.3 kDa |
| UniProt ID | Q9NWT6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm; Cytoplasm, perinuclear region |
| 蛋白大小 | 10/10 | ×1 | 10 | 349 aa / 40.3 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=58 篇 (≤60→6) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=91.4; PDB: 1H2K, 1H2L, 1H2M, 1H2N, 1IZ3, 1MZE, 1MZF |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR041667, IPR027452, IPR003347, IPR014710; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.0/180** | |
| **归一化总分** | | | **70.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm, perinuclear region | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 58 |
| PubMed broad count | 277 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FIH1 |

**关键文献**:
1. The mechanism of lncRNA SNHG1 in osteogenic differentiation via miR-497-5p/ HIF1AN axis.. *Connective tissue research*. PMID: 37966352
2. Genomic Insights into Tibetan Sheep Adaptation to Different Altitude Environments.. *International journal of molecular sciences*. PMID: 39596459
3. MicroRNA-135b regulates ERα, AR and HIF1AN and affects breast and prostate cancer cell growth.. *Molecular oncology*. PMID: 25907805
4. Ubiquitin protein E3 ligase ASB9 suppresses proliferation and promotes apoptosis in human spermatogonial stem cell line by inducing HIF1AN degradation.. *Biological research*. PMID: 36683111
5. Pinoresinol diglucoside ameliorates H/R-induced injury of cardiomyocytes by regulating miR-142-3p and HIF1AN.. *Journal of biochemical and molecular toxicology*. PMID: 35962614

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.4 |
| 高置信度残基 (pLDDT>90) 占比 | 85.1% |
| 置信残基 (pLDDT 70-90) 占比 | 7.4% |
| 中等置信 (pLDDT 50-70) 占比 | 0.6% |
| 低置信 (pLDDT<50) 占比 | 6.9% |
| 有序区域 (pLDDT>70) 占比 | 92.5% |
| 可用 PDB 条目 | 1H2K, 1H2L, 1H2M, 1H2N, 1IZ3, 1MZE, 1MZF, 1YCI, 2CGN, 2CGO |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1H2K, 1H2L, 1H2M, 1H2N, 1IZ3, 1MZE, 1MZF, 1YCI, 2CGN, 2CGO）+ AlphaFold极高置信度预测（pLDDT=91.4），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041667, IPR027452, IPR003347, IPR014710; Pfam: PF13621 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HIF1A | 0.999 | 0.991 | — |
| TNKS2 | 0.987 | 0.959 | — |
| NOTCH1 | 0.960 | 0.926 | — |
| EPAS1 | 0.937 | 0.000 | — |
| TP53BP2 | 0.935 | 0.926 | — |
| VHL | 0.911 | 0.510 | — |
| TRPV3 | 0.908 | 0.900 | — |
| PPP1R13L | 0.902 | 0.900 | — |
| PPP1R13B | 0.901 | 0.900 | — |
| TRPA1 | 0.900 | 0.900 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| INVS | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ASB13 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ASB9 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HIF1A | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:12446723 |
| OTUD7B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| ASB8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NOP58 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| APBA3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| TXLNA | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |
| KRT6C | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:29426014|imex:IM-26302| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.4 + PDB: 1H2K, 1H2L, 1H2M, 1H2N, 1IZ3,  | pLDDT=91.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm, perinuclear region / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. HIF1AN — Hypoxia-inducible factor 1-alpha inhibitor，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小349 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 58 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NWT6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166135-HIF1AN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=HIF1AN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NWT6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
