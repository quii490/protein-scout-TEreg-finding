---
type: protein-evaluation
gene: "SNIP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SNIP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SNIP1 |
| 蛋白名称 | Smad nuclear-interacting protein 1 |
| 蛋白大小 | 396 aa / 45.8 kDa |
| UniProt ID | Q8TAD8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 396 aa / 45.8 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=60 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.1; PDB: 5Z56, 5Z57, 5Z58, 6FF7, 7ABG, 7ABH, 7ABI |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050923, IPR000253, IPR008984; Pfam: PF00498 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- spliceosomal complex (GO:0005681)
- U2 snRNP (GO:0005686)
- U2-type precatalytic spliceosome (GO:0071005)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 60 |
| PubMed broad count | 84 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. TET2 suppresses vascular calcification by forming an inhibitory complex with HDAC1/2 and SNIP1 independent of demethylation.. *The Journal of clinical investigation*. PMID: 40067382
2. KMT5A-methylated SNIP1 promotes triple-negative breast cancer metastasis by activating YAP signaling.. *Nature communications*. PMID: 35449131
3. The clinical utilization of SNIP1 and its pathophysiological mechanisms in disease.. *Heliyon*. PMID: 38304835
4. LncRNA BCAN-AS1 stabilizes c-Myc via N(6)-methyladenosine-mediated binding with SNIP1 to promote pancreatic cancer.. *Cell death and differentiation*. PMID: 37726400
5. SNIP1 and PRC2 coordinate cell fates of neural progenitors during brain development.. *Nature communications*. PMID: 37553330

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.1 |
| 高置信度残基 (pLDDT>90) 占比 | 30.1% |
| 置信残基 (pLDDT 70-90) 占比 | 15.2% |
| 中等置信 (pLDDT 50-70) 占比 | 15.2% |
| 低置信 (pLDDT<50) 占比 | 39.6% |
| 有序区域 (pLDDT>70) 占比 | 45.3% |
| 可用 PDB 条目 | 5Z56, 5Z57, 5Z58, 6FF7, 7ABG, 7ABH, 7ABI, 7DVQ, 8I0P, 8I0R |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.1），有序残基占 45.3%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050923, IPR000253, IPR008984; Pfam: PF00498 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SF3B1 | 0.999 | 0.983 | — |
| RBMX2 | 0.999 | 0.995 | — |
| SNRNP200 | 0.999 | 0.992 | — |
| BUD13 | 0.999 | 0.984 | — |
| CWC22 | 0.998 | 0.965 | — |
| SNW1 | 0.998 | 0.992 | — |
| CWC27 | 0.997 | 0.963 | — |
| DHX16 | 0.997 | 0.968 | — |
| SF3B3 | 0.997 | 0.962 | — |
| SRRM2 | 0.997 | 0.971 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DVL2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RNPS1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| CDK6 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| MYC | psi-mi:"MI:0018"(two hybrid) | pubmed:17157259 |
| MAX | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17157259 |
| EBI-6620396 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:17157259 |
| EBI-5277735 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:17157259 |
| A0A384LN40 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| HSPA6 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.1 + PDB: 5Z56, 5Z57, 5Z58, 6FF7, 7ABG,  | pLDDT=66.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. SNIP1 — Smad nuclear-interacting protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小396 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 60 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=66.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TAD8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000163877-SNIP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SNIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TAD8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
