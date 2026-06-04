---
type: protein-evaluation
gene: "DTL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DTL — REJECTED (研究热度过高 (PubMed strict=207，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DTL / CDT2, CDW1, DCAF2, L2DTL, RAMP |
| 蛋白名称 | Denticleless protein homolog |
| 蛋白大小 | 730 aa / 79.5 kDa |
| UniProt ID | Q9NZJ0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli, Cytosol; UniProt: Nucleus; Nucleus membrane; Cytoplasm, cytoskeleton, microtub |
| 蛋白大小 | 10/10 | ×1 | 10 | 730 aa / 79.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=207 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=62.8; PDB: 6QC0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051865, IPR015943, IPR019775, IPR036322, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli, Cytosol | Supported |
| UniProt | Nucleus; Nucleus membrane; Cytoplasm, cytoskeleton, microtubule organizing center, centrosome; Chrom... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- centrosome (GO:0005813)
- chromosome (GO:0005694)
- Cul4-RING E3 ubiquitin ligase complex (GO:0080008)
- Cul4A-RING E3 ubiquitin ligase complex (GO:0031464)
- Cul4B-RING E3 ubiquitin ligase complex (GO:0031465)
- cytosol (GO:0005829)
- nuclear membrane (GO:0031965)
- nucleolus (GO:0005730)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 207 |
| PubMed broad count | 812 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CDT2, CDW1, DCAF2, L2DTL, RAMP |

**关键文献**:
1. DTL promotes cancer progression by PDCD4 ubiquitin-dependent degradation.. *Journal of experimental & clinical cancer research : CR*. PMID: 31409387
2. Hypoxia-induced DTL promotes the proliferation, metastasis, and sorafenib resistance of hepatocellular carcinoma through ubiquitin-mediated degradation of SLTM and subsequent Notch pathway activation.. *Cell death & disease*. PMID: 39384740
3. Unveiling novel cell clusters and biomarkers in glioblastoma and its peritumoral microenvironment at the single-cell perspective.. *Journal of translational medicine*. PMID: 38851695
4. DTL dose-dependent control of sex-dimorphic ferroptosis in liver ischemia reperfusion injury.. *Cell reports*. PMID: 40560731
5. HBx/DTL Positive Feedback Loop Promotes HBV-Related Hepatocellular Carcinoma Progression.. *Journal of medical virology*. PMID: 40062428

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 62.8 |
| 高置信度残基 (pLDDT>90) 占比 | 38.8% |
| 置信残基 (pLDDT 70-90) 占比 | 7.8% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 49.7% |
| 有序区域 (pLDDT>70) 占比 | 46.6% |
| 可用 PDB 条目 | 6QC0 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=62.8），有序残基占 46.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051865, IPR015943, IPR019775, IPR036322, IPR001680; Pfam: PF00400 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL4A | 0.999 | 0.893 | — |
| CUL4B | 0.999 | 0.888 | — |
| DDB1 | 0.999 | 0.953 | — |
| CDT1 | 0.998 | 0.748 | — |
| DCAF1 | 0.996 | 0.000 | — |
| PCNA | 0.995 | 0.983 | — |
| RBX1 | 0.995 | 0.510 | — |
| DDB2 | 0.980 | 0.292 | — |
| CDC6 | 0.963 | 0.000 | — |
| DDA1 | 0.951 | 0.471 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Tgs1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ENSMUSP00000027933.6 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Sec5 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| ci | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| Cpr100A | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| CUL4B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| WDR5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| GRWD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| DDB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| en | psi-mi:"MI:0045"(experimental interaction detectio | pubmed:unassigned4 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=62.8 + PDB: 6QC0 | pLDDT=62.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus membrane; Cytoplasm, cytoskeleton / Nucleoplasm; 额外: Nucleoli, Cytosol | 一致 |
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
1. DTL — Denticleless protein homolog，研究基础较多，新颖性有限。
2. 蛋白大小730 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 207 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=62.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 207 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NZJ0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143476-DTL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DTL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NZJ0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
