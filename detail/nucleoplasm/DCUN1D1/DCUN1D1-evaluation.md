---
type: protein-evaluation
gene: "DCUN1D1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DCUN1D1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DCUN1D1 / DCN1, DCUN1L1, RP42, SCCRO |
| 蛋白名称 | DCN1-like protein 1 |
| 蛋白大小 | 259 aa / 30.1 kDa |
| UniProt ID | Q96GG9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 259 aa / 30.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=92.1; PDB: 3TDU, 3TDZ, 4P5O, 5UFI, 5V83, 5V86, 5V88 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR014764, IPR042460, IPR005176, IPR009060; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Approved |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 75 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DCN1, DCUN1L1, RP42, SCCRO |

**关键文献**:
1. Disruption of the cerebrospinal fluid-plasma protein balance in cognitive impairment and aging.. *Nature medicine*. PMID: 40665050
2. DCUN1D1 and neddylation: Potential targets for cancer therapy.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 38885797
3. 3q26 Amplifications in Cervical Squamous Carcinomas.. *Current oncology (Toronto, Ont.)*. PMID: 34436017
4. DCUN1D1, a new molecule involved in depigmentation via upregulating CXCL10.. *Experimental dermatology*. PMID: 36541112
5. Mouse DCUN1D1 (SCCRO) is required for spermatogenetic individualization.. *PloS one*. PMID: 30653527

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.1 |
| 高置信度残基 (pLDDT>90) 占比 | 81.5% |
| 置信残基 (pLDDT 70-90) 占比 | 12.4% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 1.2% |
| 有序区域 (pLDDT>70) 占比 | 93.9% |
| 可用 PDB 条目 | 3TDU, 3TDZ, 4P5O, 5UFI, 5V83, 5V86, 5V88, 6B5Q, 6BG3, 6BG5 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3TDU, 3TDZ, 4P5O, 5UFI, 5V83, 5V86, 5V88, 6B5Q, 6BG3, 6BG5）+ AlphaFold极高置信度预测（pLDDT=92.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR014764, IPR042460, IPR005176, IPR009060; Pfam: PF03556, PF14555 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL1 | 0.999 | 0.993 | — |
| UBE2M | 0.999 | 0.993 | — |
| RBX1 | 0.998 | 0.969 | — |
| NEDD8 | 0.996 | 0.816 | — |
| CUL3 | 0.987 | 0.910 | — |
| UBE2F | 0.973 | 0.642 | — |
| CAND1 | 0.969 | 0.834 | — |
| CUL2 | 0.963 | 0.849 | — |
| CUL4A | 0.957 | 0.825 | — |
| CUL4B | 0.953 | 0.825 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRIM39 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| SCCRO | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| DAZAP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| Dmel\CG18745 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16603075|imex:IM-19959 |
| CUL1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| NEDD8 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.1 + PDB: 3TDU, 3TDZ, 4P5O, 5UFI, 5V83,  | pLDDT=92.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DCUN1D1 — DCN1-like protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小259 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96GG9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000043093-DCUN1D1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DCUN1D1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96GG9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
