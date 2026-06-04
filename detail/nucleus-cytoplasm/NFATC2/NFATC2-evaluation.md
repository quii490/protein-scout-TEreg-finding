---
type: protein-evaluation
gene: "NFATC2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NFATC2 — REJECTED (研究热度过高 (PubMed strict=379，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NFATC2 / NFAT1, NFATP |
| 蛋白名称 | Nuclear factor of activated T-cells, cytoplasmic 2 |
| 蛋白大小 | 925 aa / 100.1 kDa |
| UniProt ID | Q13469 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 925 aa / 100.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=379 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=56.7; PDB: 1A02, 1OWR, 1P7H, 1PZU, 1S9K, 2AS5, 2O93 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013783, IPR014756, IPR002909, IPR008366, IPR008 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **76.0/180** | |
| **归一化总分** | | | **42.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- ribonucleoprotein complex (GO:1990904)
- transcription factor AP-1 complex (GO:0035976)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 379 |
| PubMed broad count | 877 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NFAT1, NFATP |

**关键文献**:
1. Deletion of SNX9 alleviates CD8 T cell exhaustion for effective cellular cancer immunotherapy.. *Nature communications*. PMID: 36732507
2. Robust gene expression programs underlie recurrent cell states and phenotype switching in melanoma.. *Nature cell biology*. PMID: 32753671
3. Early methionine availability attenuates T cell exhaustion.. *Nature immunology*. PMID: 40702340
4. Single cell analysis reveals the roles and regulatory mechanisms of type-I interferons in Parkinson's disease.. *Cell communication and signaling : CCS*. PMID: 38566100
5. Histone lactylation promotes rheumatoid arthritis progression by increasing NFATc2 expression and the production of anti-lactylated histone autoantibodies.. *Nature communications*. PMID: 41073397

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 56.7 |
| 高置信度残基 (pLDDT>90) 占比 | 25.5% |
| 置信残基 (pLDDT 70-90) 占比 | 6.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.8% |
| 低置信 (pLDDT<50) 占比 | 63.6% |
| 有序区域 (pLDDT>70) 占比 | 31.7% |
| 可用 PDB 条目 | 1A02, 1OWR, 1P7H, 1PZU, 1S9K, 2AS5, 2O93, 3QRF, 8OW4, 8R07 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=56.7），有序残基占 31.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013783, IPR014756, IPR002909, IPR008366, IPR008967; Pfam: PF16179, PF00554 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Litaf | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Notch4 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Pold2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Anp32a | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Tfg | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Capn2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Irf5 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Qrich1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| - | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:16873067|imex:IM-19878 |
| Il2 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:16873067|imex:IM-19878 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=56.7 + PDB: 1A02, 1OWR, 1P7H, 1PZU, 1S9K,  | pLDDT=56.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NFATC2 — Nuclear factor of activated T-cells, cytoplasmic 2，研究基础较多，新颖性有限。
2. 蛋白大小925 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 379 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=56.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 379 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13469
- Protein Atlas: https://www.proteinatlas.org/ENSG00000101096-NFATC2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NFATC2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13469
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
