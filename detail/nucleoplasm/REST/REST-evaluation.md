---
type: protein-evaluation
gene: "REST"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## REST — REJECTED (研究热度过高 (PubMed strict=16337，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | REST / NRSF, XBR |
| 蛋白名称 | RE1-silencing transcription factor |
| 蛋白大小 | 1097 aa / 121.9 kDa |
| UniProt ID | Q13127 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm; Cytoplasm; Nucleus; Cytoplasm |
| 蛋白大小 | 8/10 | ×1 | 8 | 1097 aa / 121.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=16337 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=48.9; PDB: 2CZY, 6DU2, 6DU3 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR057281, IPR050688, IPR036236, IPR013087; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 10 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm; Cytoplasm; Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription repressor complex (GO:0017053)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16337 |
| PubMed broad count | 213807 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NRSF, XBR |

**关键文献**:
1. REST and stress resistance in ageing and Alzheimer's disease.. *Nature*. PMID: 24670762
2. Kurarinone alleviated Parkinson's disease via stabilization of epoxyeicosatrienoic acids in animal model.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 35217618
3. Epigenetics and epilepsy.. *Epilepsia*. PMID: 23216574
4. Erianin induces ferroptosis in GSCs via REST/LRSAM1 mediated SLC40A1 ubiquitination to overcome TMZ resistance.. *Cell death & disease*. PMID: 39039049
5. Impaired neural stress resistance and loss of REST in bipolar disorder.. *Molecular psychiatry*. PMID: 37938767

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 48.9 |
| 高置信度残基 (pLDDT>90) 占比 | 1.8% |
| 置信残基 (pLDDT 70-90) 占比 | 18.4% |
| 中等置信 (pLDDT 50-70) 占比 | 11.9% |
| 低置信 (pLDDT<50) 占比 | 67.8% |
| 有序区域 (pLDDT>70) 占比 | 20.2% |
| 可用 PDB 条目 | 2CZY, 6DU2, 6DU3 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=48.9），有序残基占 20.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR057281, IPR050688, IPR036236, IPR013087; Pfam: PF00096, PF24540 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RCOR1 | 0.999 | 0.738 | — |
| KDM1A | 0.995 | 0.049 | — |
| HDAC1 | 0.994 | 0.535 | — |
| HTT | 0.991 | 0.095 | — |
| CTDSP1 | 0.987 | 0.926 | — |
| SIN3A | 0.973 | 0.540 | — |
| SIN3B | 0.971 | 0.930 | — |
| HDAC2 | 0.964 | 0.328 | — |
| EHMT2 | 0.926 | 0.537 | — |
| BTRC | 0.885 | 0.842 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| SMARCE1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12192000|imex:IM-18886 |
| SMARCA4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12192000|imex:IM-18886 |
| SMARCC2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:12192000|imex:IM-18886 |
| Nanog | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17093407|imex:IM-20293 |
| H2BC21 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| H2BC5 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| Wiz | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |
| Ewsr1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:20211142|doi:10.1016/j. |
| P | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:unassigned2293|imex:IM- |
| AFG2A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:38554706|imex:IM-30175 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 10
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 10 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=48.9 + PDB: 2CZY, 6DU2, 6DU3 | pLDDT=48.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Cytoplasm; Nucleus; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 10 interactions | 数据充分 |

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
1. REST — RE1-silencing transcription factor，研究基础较多，新颖性有限。
2. 蛋白大小1097 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 16337 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=48.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 16337 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13127
- Protein Atlas: https://www.proteinatlas.org/ENSG00000084093-REST/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=REST
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13127
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
