---
type: protein-evaluation
gene: "TLX3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TLX3 — REJECTED (研究热度过高 (PubMed strict=105，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TLX3 / HOX11L2 |
| 蛋白名称 | T-cell leukemia homeobox protein 3 |
| 蛋白大小 | 291 aa / 31.9 kDa |
| UniProt ID | O43711 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 291 aa / 31.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=105 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR001356, IPR020479, IPR017970, IPR009057, IPR042 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.0/180** | |
| **归一化总分** | | | **48.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 105 |
| PubMed broad count | 203 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: HOX11L2 |

**关键文献**:
1. T-Cell Acute Lymphoblastic Leukemia: Biomarkers and Their Clinical Usefulness.. *Genes*. PMID: 34440292
2. Tlx3 mediates neuronal differentiation and proper condensation of the developing trigeminal ganglion.. *Developmental biology*. PMID: 39019425
3. Towards methylation-based redefinition of TAL1 positive T-cell acute lymphoblastic leukaemia (T-ALL).. *Leukemia*. PMID: 40781485
4. PHF6 Mutations in Hematologic Malignancies.. *Frontiers in oncology*. PMID: 34381727
5. Tlx3 controls the development of C-low threshold mechanoreceptors.. *Neuroreport*. PMID: 36062515

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.8 |
| 高置信度残基 (pLDDT>90) 占比 | 25.1% |
| 置信残基 (pLDDT 70-90) 占比 | 9.3% |
| 中等置信 (pLDDT 50-70) 占比 | 43.6% |
| 低置信 (pLDDT<50) 占比 | 22.0% |
| 有序区域 (pLDDT>70) 占比 | 34.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.8），有序残基占 34.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001356, IPR020479, IPR017970, IPR009057, IPR042247; Pfam: PF00046 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PHF6 | 0.896 | 0.045 | — |
| LYL1 | 0.852 | 0.046 | — |
| NUP214 | 0.848 | 0.000 | — |
| TAL1 | 0.825 | 0.046 | — |
| LMO1 | 0.824 | 0.104 | — |
| BCL11B | 0.814 | 0.052 | — |
| RANBP17 | 0.798 | 0.000 | — |
| LMO2 | 0.790 | 0.196 | — |
| ABL1 | 0.739 | 0.048 | — |
| LMX1B | 0.674 | 0.104 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| LMO2 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| ETS1 | psi-mi:"MI:0663"(confocal microscopy) | pubmed:22516263|imex:IM-17328 |
| ENSP00000296921.5 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:22516263|imex:IM-17328 |
| HMGN2 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| SMU1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| APBB1IP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| MORN5 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| THTPA | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| ROR2 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| PLAAT1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.8 + PDB: 无 | pLDDT=66.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TLX3 — T-cell leukemia homeobox protein 3，研究基础较多，新颖性有限。
2. 蛋白大小291 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 105 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=66.8），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 105 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O43711
- Protein Atlas: https://www.proteinatlas.org/ENSG00000164438-TLX3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TLX3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O43711
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
