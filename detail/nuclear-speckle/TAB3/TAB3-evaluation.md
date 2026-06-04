---
type: protein-evaluation
gene: "TAB3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TAB3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TAB3 / MAP3K7IP3 |
| 蛋白名称 | TGF-beta-activated kinase 1 and MAP3K7-binding protein 3 |
| 蛋白大小 | 712 aa / 78.7 kDa |
| UniProt ID | Q8N5C8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear speckles, Cytosol; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 712 aa / 78.7 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=80 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003892, IPR041911, IPR001876, IPR036443; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles, Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endosome membrane (GO:0010008)
- extracellular exosome (GO:0070062)
- plasma membrane (GO:0005886)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 80 |
| PubMed broad count | 147 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MAP3K7IP3 |

**关键文献**:
1. Inhibition of METTL3 attenuates renal injury and inflammation by alleviating TAB3 m6A modifications via IGF2BP2-dependent mechanisms.. *Science translational medicine*. PMID: 35417191
2. TAK1-binding protein 2 (TAB2) and TAB3 are redundantly required for TLR-induced cytokine production in macrophages.. *International immunology*. PMID: 38567483
3. TAB3 upregulates PIM1 expression by directly activating the TAK1-STAT3 complex to promote colorectal cancer growth.. *Experimental cell research*. PMID: 32229191
4. Loss of ESRP2 Activates TAK1-MAPK Signaling through the Fetal RNA-Splicing Program to Promote Hepatocellular Carcinoma Progression.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 37985644
5. Post-Translational Modifications of the TAK1-TAB Complex.. *International journal of molecular sciences*. PMID: 28106845

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.3 |
| 高置信度残基 (pLDDT>90) 占比 | 13.2% |
| 置信残基 (pLDDT 70-90) 占比 | 10.3% |
| 中等置信 (pLDDT 50-70) 占比 | 10.1% |
| 低置信 (pLDDT<50) 占比 | 66.4% |
| 有序区域 (pLDDT>70) 占比 | 23.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=53.3），有序残基占 23.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003892, IPR041911, IPR001876, IPR036443; Pfam: PF02845 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TRAF6 | 0.999 | 0.848 | — |
| TAB2 | 0.999 | 0.731 | — |
| TAB1 | 0.999 | 0.821 | — |
| IKBKG | 0.999 | 0.994 | — |
| MAP3K7 | 0.999 | 0.929 | — |
| RIPK1 | 0.987 | 0.097 | — |
| IKBKB | 0.986 | 0.325 | — |
| TRAF3 | 0.977 | 0.118 | — |
| MYD88 | 0.975 | 0.000 | — |
| RIPK2 | 0.974 | 0.097 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12496252 |
| MAP3K7 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| MAP3K7CL | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ENSP00000368215.1 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| TAB2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| TAB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:21903422|imex:IM-17322 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EMILIN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28169297|imex:IM-25584 |
| PIN1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.3 + PDB: 无 | pLDDT=53.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear speckles, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐

**核心优势**:
1. TAB3 — TGF-beta-activated kinase 1 and MAP3K7-binding protein 3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小712 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 80 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=53.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N5C8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157625-TAB3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TAB3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N5C8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
