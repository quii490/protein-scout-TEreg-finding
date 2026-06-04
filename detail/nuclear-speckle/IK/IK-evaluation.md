---
type: protein-evaluation
gene: "IK"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## IK — REJECTED (研究热度过高 (PubMed strict=925，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IK / RED, RER |
| 蛋白名称 | Protein Red |
| 蛋白大小 | 557 aa / 65.6 kDa |
| UniProt ID | Q13123 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear speckles; UniProt: Nucleus; Nucleus, nucleoplasm; Chromosome; Cytoplasm, cytosk |
| 蛋白大小 | 10/10 | ×1 | 10 | 557 aa / 65.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=925 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.1; PDB: 5O9Z, 6Q8I, 8QO9, 8QZS |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039896, IPR012492, IPR012916; Pfam: PF07807, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear speckles | Enhanced |
| UniProt | Nucleus; Nucleus, nucleoplasm; Chromosome; Cytoplasm, cytoskeleton, spindle pole | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome (GO:0005694)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- spindle pole (GO:0000922)
- U2-type precatalytic spliceosome (GO:0071005)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 925 |
| PubMed broad count | 10450 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RED, RER |

**关键文献**:
1. Targeting Ca(2+)-activated K(+) channels in glioma.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 40484048
2. EPAC1 and 2 inhibit K(+) currents via PLC/PKC and NOS/PKG pathways in rat ventricular cardiomyocytes.. *American journal of physiology. Cell physiology*. PMID: 38985989
3. Investigating cytotoxic and inflammatory human IL-7 receptor low effector memory CD8(+) T cells in lupus.. *EBioMedicine*. PMID: 40857939
4. Ikaros gene expression and leukemia.. *Leukemia & lymphoma*. PMID: 11908734
5. Decreased coronary arteriolar response to K(Ca) channel opener after cardioplegic arrest in diabetic patients.. *Molecular and cellular biochemistry*. PMID: 29305679

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.1 |
| 高置信度残基 (pLDDT>90) 占比 | 10.4% |
| 置信残基 (pLDDT 70-90) 占比 | 40.2% |
| 中等置信 (pLDDT 50-70) 占比 | 29.3% |
| 低置信 (pLDDT<50) 占比 | 20.1% |
| 有序区域 (pLDDT>70) 占比 | 50.6% |
| 可用 PDB 条目 | 5O9Z, 6Q8I, 8QO9, 8QZS |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=68.1），有序残基占 50.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039896, IPR012492, IPR012916; Pfam: PF07807, PF07808 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SMU1 | 0.999 | 0.997 | — |
| MFAP1 | 0.995 | 0.936 | — |
| PRPF6 | 0.995 | 0.936 | — |
| EFTUD2 | 0.994 | 0.936 | — |
| PRPF38A | 0.990 | 0.800 | — |
| SF3B3 | 0.989 | 0.900 | — |
| PRPF8 | 0.986 | 0.839 | — |
| PRPF3 | 0.985 | 0.800 | — |
| LSM4 | 0.985 | 0.800 | — |
| SF3B1 | 0.985 | 0.800 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CHD3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| KAT5 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| PFN2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| SUPT5H | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| NUP62 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21150319|imex:IM-16995 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| sbcB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| rev | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| GRB2 | psi-mi:"MI:0018"(two hybrid) | pubmed:18624398|imex:IM-19021 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.1 + PDB: 5O9Z, 6Q8I, 8QO9, 8QZS | pLDDT=68.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleoplasm; Chromosome; Cytopla / Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

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
1. IK — Protein Red，研究基础较多，新颖性有限。
2. 蛋白大小557 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 925 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=68.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 925 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13123
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113141-IK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13123
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
