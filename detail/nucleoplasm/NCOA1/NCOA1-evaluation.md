---
type: protein-evaluation
gene: "NCOA1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NCOA1 — REJECTED (研究热度过高 (PubMed strict=179，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NCOA1 / BHLHE74, SRC1 |
| 蛋白名称 | Nuclear receptor coactivator 1 |
| 蛋白大小 | 1441 aa / 156.8 kDa |
| UniProt ID | Q15788 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; 额外: Vesicles, Plasma membrane; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1441 aa / 156.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=179 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=46.7; PDB: 1FM6, 1FM9, 1K4W, 1K74, 1K7L, 1KV6, 1N4H |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011598, IPR056193, IPR036638, IPR010011, IPR028 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.5/180** | |
| **归一化总分** | | | **42.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol; 额外: Vesicles, Plasma membrane | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)
- protein-containing complex (GO:0032991)
- RNA polymerase II transcription regulator complex (GO:0090575)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 179 |
| PubMed broad count | 894 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BHLHE74, SRC1 |

**关键文献**:
1. Explore the mechanism and substance basis of Mahuang FuziXixin Decoction for the treatment of lung cancer based on network pharmacology and molecular docking.. *Computers in biology and medicine*. PMID: 36399857
2. Targeted Inhibition of the NCOA1/STAT6 Protein-Protein Interaction.. *Journal of the American Chemical Society*. PMID: 29090910
3. Retinoic acid receptor assembly dynamics governs dual functions in cochlear organogenesis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 40577120
4. Tai/NCOA2 suppresses the Hedgehog pathway by directly targeting the transcription factor Ci/GLI.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 39531503
5. NCOA1 is a gatekeeper of the sexually dimorphic thermogenic activity of white adipose tissue.. *Nature communications*. PMID: 41559022

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 46.7 |
| 高置信度残基 (pLDDT>90) 占比 | 9.2% |
| 置信残基 (pLDDT 70-90) 占比 | 11.1% |
| 中等置信 (pLDDT 50-70) 占比 | 7.5% |
| 低置信 (pLDDT<50) 占比 | 72.2% |
| 有序区域 (pLDDT>70) 占比 | 20.3% |
| 可用 PDB 条目 | 1FM6, 1FM9, 1K4W, 1K74, 1K7L, 1KV6, 1N4H, 1NQ7, 1NRL, 1P8D |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=46.7），有序残基占 20.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011598, IPR056193, IPR036638, IPR010011, IPR028819; Pfam: PF23172, PF07469, PF16665 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPARG | 0.999 | 0.992 | — |
| CREBBP | 0.999 | 0.984 | — |
| RXRA | 0.999 | 0.995 | — |
| EP300 | 0.999 | 0.792 | — |
| ESR1 | 0.999 | 0.997 | — |
| ESR2 | 0.999 | 0.984 | — |
| NR1I2 | 0.998 | 0.989 | — |
| PPARA | 0.998 | 0.985 | — |
| STAT6 | 0.997 | 0.983 | — |
| NCOA2 | 0.997 | 0.735 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000385216.1 | psi-mi:"MI:0114"(x-ray crystallography) | imex:IM-25512|pubmed:23602807 |
| clpB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Nfkb1 | psi-mi:"MI:0018"(two hybrid) | pubmed:9556555|imex:IM-19559 |
| Nr3c1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12917342|imex:IM-19964 |
| AR | psi-mi:"MI:0018"(two hybrid) | pubmed:17353003|imex:IM-18874 |
| ESRRA | psi-mi:"MI:0053"(fluorescence polarization spectro | imex:IM-26396|pubmed:15337744 |
| BRME1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NR1I3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TNIK | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:31413325|imex:IM-26801 |
| THRB | psi-mi:"MI:0096"(pull down) | pubmed:9605924|imex:IM-27030 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=46.7 + PDB: 1FM6, 1FM9, 1K4W, 1K74, 1K7L,  | pLDDT=46.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Cytosol; 额外: Vesicles, Plasma membran | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NCOA1 — Nuclear receptor coactivator 1，研究基础较多，新颖性有限。
2. 蛋白大小1441 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 179 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=46.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 179 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15788
- Protein Atlas: https://www.proteinatlas.org/ENSG00000084676-NCOA1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NCOA1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15788
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
