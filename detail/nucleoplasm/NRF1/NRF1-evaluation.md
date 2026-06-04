---
type: protein-evaluation
gene: "NRF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NRF1 — REJECTED (研究热度过高 (PubMed strict=1594，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NRF1 |
| 蛋白名称 | Nuclear respiratory factor 1 |
| 蛋白大小 | 503 aa / 53.5 kDa |
| UniProt ID | Q16656 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 503 aa / 53.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=1594 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=57.5; PDB: 8K3D, 8K4L |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039142, IPR019525; Pfam: PF10491 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1594 |
| PubMed broad count | 2349 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Sugar-mediated non-canonical ubiquitination impairs Nrf1/NFE2L1 activation.. *Molecular cell*. PMID: 39116872
2. NRF1-mediated microglial activation triggers high-altitude cerebral edema.. *Journal of molecular cell biology*. PMID: 35704676
3. Caveolin-1 accelerates hypoxia-induced endothelial dysfunction in high-altitude cerebral edema.. *Cell communication and signaling : CCS*. PMID: 36253854
4. Nrf1 promotes heart regeneration and repair by regulating proteostasis and redox balance.. *Nature communications*. PMID: 34489413
5. Songorine promotes cardiac mitochondrial biogenesis via Nrf2 induction during sepsis.. *Redox biology*. PMID: 33189984

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.5 |
| 高置信度残基 (pLDDT>90) 占比 | 15.1% |
| 置信残基 (pLDDT 70-90) 占比 | 20.1% |
| 中等置信 (pLDDT 50-70) 占比 | 17.1% |
| 低置信 (pLDDT<50) 占比 | 47.7% |
| 有序区域 (pLDDT>70) 占比 | 35.2% |
| 可用 PDB 条目 | 8K3D, 8K4L |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.5），有序残基占 35.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039142, IPR019525; Pfam: PF10491 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PPARGC1A | 0.999 | 0.292 | — |
| PPARGC1B | 0.991 | 0.000 | — |
| TFAM | 0.987 | 0.000 | — |
| PPRC1 | 0.937 | 0.292 | — |
| FOXO3 | 0.933 | 0.000 | — |
| CYCS | 0.899 | 0.000 | — |
| GABPA | 0.887 | 0.000 | — |
| GABPB1 | 0.849 | 0.000 | — |
| ESRRA | 0.849 | 0.000 | — |
| HCFC1 | 0.830 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VTC1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| UBC7 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| NFE2L1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| lysU | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| sph | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CSN5A | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| MRS2-2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| ATP1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| TCP13 | psi-mi:"MI:0397"(two hybrid array) | pubmed:21798944|imex:IM-16043 |
| NYV1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:11823419|imex:IM-19556 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.5 + PDB: 8K3D, 8K4L | pLDDT=57.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NRF1 — Nuclear respiratory factor 1，研究基础较多，新颖性有限。
2. 蛋白大小503 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 1594 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 1594 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16656
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106459-NRF1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NRF1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16656
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
