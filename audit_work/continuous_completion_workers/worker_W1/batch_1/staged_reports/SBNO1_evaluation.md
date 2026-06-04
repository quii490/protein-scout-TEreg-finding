---
type: protein-evaluation
gene: "SBNO1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## SBNO1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SBNO1 / MOP3 |
| 蛋白名称 | Protein strawberry notch homolog 1 |
| 蛋白大小 | 1393 aa / 154.3 kDa |
| UniProt ID | A3KN83 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1393 aa / 154.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=13 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR027417, IPR057332, IPR026937, IPR026741, IPR039 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.0/180** | |
| **归一化总分** | | | **73.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（批量模式），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MOP3 |

**关键文献**:
1. The plasma peptides of sepsis.. *Clinical proteomics*. PMID: 32636717
2. Study of Strawberry Notch homolog 1 and 2 expression in human glioblastoma.. *Journal of neuro-oncology*. PMID: 36695974
3. Involvement of strawberry notch homologue 1 in neurite outgrowth of cortical neurons.. *Development, growth & differentiation*. PMID: 36057539
4. Expression of strawberry notch family genes during zebrafish embryogenesis.. *Developmental dynamics : an official publication of the American Association of Anatomists*. PMID: 20503374
5. Genomic structural variants are linked with intellectual disability.. *Journal of neural transmission (Vienna, Austria : 1996)*. PMID: 25626716

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.3 |
| 高置信度残基 (pLDDT>90) 占比 | 17.9% |
| 置信残基 (pLDDT 70-90) 占比 | 42.6% |
| 中等置信 (pLDDT 50-70) 占比 | 7.9% |
| 低置信 (pLDDT<50) 占比 | 31.6% |
| 有序区域 (pLDDT>70) 占比 | 60.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（批量模式），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.3），有序残基占 60.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027417, IPR057332, IPR026937, IPR026741, IPR039187; Pfam: PF13872, PF13871, PF25373 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RASGEF1A | 0.812 | 0.000 | — |
| RIOK1 | 0.810 | 0.000 | — |
| RIOX1 | 0.796 | 0.000 | — |
| TGFBRAP1 | 0.790 | 0.000 | — |
| RIF1 | 0.660 | 0.000 | — |
| PDS5A | 0.636 | 0.000 | — |
| CDK2AP1 | 0.626 | 0.000 | — |
| PBDC1 | 0.618 | 0.220 | — |
| LTN1 | 0.605 | 0.000 | — |
| H7C0V5_HUMAN | 0.603 | 0.054 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| fadL | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CDK8 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| H2BC9 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| IVNS1ABP | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| SPAG9 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| MCM2 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| GTF3C4 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| EPS15L1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| USP15 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| MCM6 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.3 + PDB: 无 | pLDDT=67.3, v6 | 仅预测 |
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

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. SBNO1 — Protein strawberry notch homolog 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1393 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=67.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/A3KN83
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139697-SBNO1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SBNO1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/A3KN83
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
