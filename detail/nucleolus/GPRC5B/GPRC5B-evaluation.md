---
type: protein-evaluation
gene: "GPRC5B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## GPRC5B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPRC5B / RAIG2 |
| 蛋白名称 | G-protein coupled receptor family C group 5 member B |
| 蛋白大小 | 403 aa / 44.8 kDa |
| UniProt ID | Q9NZH0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; 额外: Nucleoplasm, Nucleoli; UniProt: Cell membrane; Cytoplasmic vesicle membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 403 aa / 44.8 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=78 篇 (≤80→4) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017978, IPR051753; Pfam: PF00003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **103.5/180** | |
| **归一化总分** | | | **57.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm, Nucleoli | Supported |
| UniProt | Cell membrane; Cytoplasmic vesicle membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cell surface (GO:0009986)
- cytoplasmic vesicle membrane (GO:0030659)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular space (GO:0005615)
- membrane raft (GO:0045121)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 78 |
| PubMed broad count | 91 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RAIG2 |

**关键文献**:
1. Aquaporin-4 and GPRC5B: old and new players in controlling brain oedema.. *Brain : a journal of neurology*. PMID: 37143309
2. GPRC5B protects osteoarthritis by regulation of autophagy signaling.. *Acta pharmaceutica Sinica. B*. PMID: 37521864
3. Orphan G protein-coupled receptor GPRC5B controls macrophage function by facilitating prostaglandin E receptor 2 signaling.. *Nature communications*. PMID: 39920161
4. GPRC5B preserves a mature β cell state in obesity by controlling MafA expression.. *JCI insight*. PMID: 40906536
5. GPRC5B (G protein-coupled receptor class C group 5 member B) suppresses glucose starvation-induced apoptosis in head-and-neck squamous cell carcinoma.. *Biomedical research (Tokyo, Japan)*. PMID: 36682796

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.4 |
| 高置信度残基 (pLDDT>90) 占比 | 40.4% |
| 置信残基 (pLDDT 70-90) 占比 | 19.9% |
| 中等置信 (pLDDT 50-70) 占比 | 16.1% |
| 低置信 (pLDDT<50) 占比 | 23.6% |
| 有序区域 (pLDDT>70) 占比 | 60.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=74.4，有序区 60.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017978, IPR051753; Pfam: PF00003 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IQCK | 0.675 | 0.000 | — |
| FANCL | 0.625 | 0.000 | — |
| GPR158 | 0.594 | 0.000 | — |
| FPGT-TNNI3K | 0.586 | 0.000 | — |
| TNNI3K | 0.586 | 0.000 | — |
| ZNF608 | 0.584 | 0.000 | — |
| SEC16B | 0.572 | 0.000 | — |
| TMEM160 | 0.570 | 0.000 | — |
| NEGR1 | 0.566 | 0.000 | — |
| GNPDA2 | 0.533 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| C11orf71 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| CSGALNACT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSP90B1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| LPAR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TMEM171 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ADGRE5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IPPK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CD70 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| STXBP3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SDCBP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.4 + PDB: 无 | pLDDT=74.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell membrane; Cytoplasmic vesicle membrane / Vesicles; 额外: Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. GPRC5B — G-protein coupled receptor family C group 5 member B，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小403 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 78 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NZH0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167191-GPRC5B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPRC5B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NZH0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
