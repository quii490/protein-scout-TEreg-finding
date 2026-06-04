---
type: protein-evaluation
gene: "RTN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RTN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RTN1 / NSP |
| 蛋白名称 | Reticulon-1 |
| 蛋白大小 | 776 aa / 83.6 kDa |
| UniProt ID | Q16799 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum; 额外: Nuclear bodies; UniProt: Endoplasmic reticulum membrane; Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 776 aa / 83.6 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=73 篇 (≤80→4) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR003388, IPR046964; Pfam: PF02453 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **100.0/180** | |
| **归一化总分** | | | **55.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum; 额外: Nuclear bodies | Supported |
| UniProt | Endoplasmic reticulum membrane; Golgi apparatus membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- dendrite (GO:0030425)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- Golgi membrane (GO:0000139)
- neuron projection (GO:0043005)
- neuronal cell body (GO:0043025)
- nuclear body (GO:0016604)
- postsynaptic density (GO:0014069)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 73 |
| PubMed broad count | 163 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NSP |

**关键文献**:
1. RTN1 and RTN3 protein are differentially associated with senile plaques in Alzheimer's brains.. *Scientific reports*. PMID: 28733667
2. RTN1-C mediates cerebral ischemia/reperfusion injury via ER stress and mitochondria-associated apoptosis pathways.. *Cell death & disease*. PMID: 28981095
3. HTT (huntingtin) and RAB7 co-migrate retrogradely on a signaling LAMP1-containing late endosome during axonal injury.. *Autophagy*. PMID: 36048753
4. Gene networks in neurodegenerative disorders.. *Life sciences*. PMID: 28623007
5. Shared senescence-associated gene networks in PCOS and T2DM: biomarker identification and functional validation.. *Frontiers in endocrinology*. PMID: 41079183

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.1 |
| 高置信度残基 (pLDDT>90) 占比 | 12.0% |
| 置信残基 (pLDDT 70-90) 占比 | 12.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 68.6% |
| 有序区域 (pLDDT>70) 占比 | 24.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=48.1），有序残基占 24.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR003388, IPR046964; Pfam: PF02453 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SPAST | 0.904 | 0.071 | — |
| REEP5 | 0.902 | 0.126 | — |
| ATL3 | 0.865 | 0.075 | — |
| ATL2 | 0.862 | 0.075 | — |
| RTN4 | 0.849 | 0.697 | — |
| ATL1 | 0.848 | 0.075 | — |
| RTN2 | 0.832 | 0.476 | — |
| TMEM33 | 0.825 | 0.144 | — |
| BACE1 | 0.757 | 0.175 | — |
| MANF | 0.740 | 0.292 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Rtnl1 | psi-mi:"MI:0963"(interactome parallel affinity cap | pubmed:21447707|imex:IM-17304 |
| D6VSL4 | psi-mi:"MI:0111"(dihydrofolate reductase reconstru | pubmed:31454312|imex:IM-26944 |
| PLEKHF2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| PEP4 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| Cht9 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| SSA2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSB1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| ADH1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SSA1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| TEF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.1 + PDB: 无 | pLDDT=48.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Golgi apparatus me / Endoplasmic reticulum; 额外: Nuclear bodies | 一致 |
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
1. RTN1 — Reticulon-1，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小776 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 73 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=48.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16799
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139970-RTN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RTN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16799
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
