---
type: protein-evaluation
gene: "MYCBP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MYCBP2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MYCBP2 / KIAA0916, PAM |
| 蛋白名称 | E3 ubiquitin-protein ligase MYCBP2 |
| 蛋白大小 | 4678 aa / 513.6 kDa |
| UniProt ID | O75592 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles, Cytosol; UniProt: Nucleus; Cell projection, axon; Cytoplasm, cytoskeleton |
| 蛋白大小 | 0/10 | ×1 | 0 | 4678 aa / 513.6 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=56 篇 (≤60→6) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 5O6C, 6T7F |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004939, IPR017868, IPR008979, IPR013783, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles, Cytosol | Supported |
| UniProt | Nucleus; Cell projection, axon; Cytoplasm, cytoskeleton | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon (GO:0030424)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- microtubule cytoskeleton (GO:0015630)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 56 |
| PubMed broad count | 105 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0916, PAM |

**关键文献**:
1. Loss-of-function variants in MYCBP2 cause neurobehavioural phenotypes and corpus callosum defects.. *Brain : a journal of neurology*. PMID: 36200388
2. Targeting autophagy using small-molecule compounds to improve potential therapy of Parkinson's disease.. *Acta pharmaceutica Sinica. B*. PMID: 34729301
3. Activity-based E3 ligase profiling uncovers an E3 ligase with esterification activity.. *Nature*. PMID: 29643511
4. Annexin A1 binds PDZ and LIM domain 7 to inhibit adipogenesis and prevent obesity.. *Signal transduction and targeted therapy*. PMID: 39174522
5. Ubiquitin ligase and signalling hub MYCBP2 is required for efficient EPHB2 tyrosine kinase receptor function.. *eLife*. PMID: 38289221

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 5O6C, 6T7F |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004939, IPR017868, IPR008979, IPR013783, IPR014756; Pfam: PF03256, PF08005, PF00415 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FBXO45 | 0.999 | 0.942 | — |
| UBE2D2 | 0.935 | 0.918 | — |
| MYC | 0.923 | 0.565 | — |
| UBC | 0.913 | 0.900 | — |
| RPS27A | 0.908 | 0.900 | — |
| UBB | 0.902 | 0.900 | — |
| UBA52 | 0.900 | 0.900 | — |
| SKP1 | 0.894 | 0.460 | — |
| LRPAP1 | 0.851 | 0.000 | — |
| FBXW7 | 0.793 | 0.703 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| YWHAB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| BAK1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TTN | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| tktA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| glgA | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| mtaD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000444596.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A0F7RHU0 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A1Q4M0N4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 5O6C, 6T7F | pLDDT=0, v? | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cell projection, axon; Cytoplasm, cytoske / Nucleoplasm; 额外: Vesicles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. MYCBP2 — E3 ubiquitin-protein ligase MYCBP2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小4678 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 56 篇，已有一定研究基础
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75592
- Protein Atlas: https://www.proteinatlas.org/ENSG00000005810-MYCBP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MYCBP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75592
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
