---
type: protein-evaluation
gene: "TMC8"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TMC8 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TMC8 / EVER2, EVIN2 |
| 蛋白名称 | Transmembrane channel-like protein 8 |
| 蛋白大小 | 726 aa / 81.6 kDa |
| UniProt ID | Q8IU68 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Golgi apparatus; UniProt: Endoplasmic reticulum membrane; Golgi apparatus membrane; Nu |
| 蛋白大小 | 10/10 | ×1 | 10 | 726 aa / 81.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=39 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=75.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR038900, IPR012496; Pfam: PF07810 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus | Uncertain |
| UniProt | Endoplasmic reticulum membrane; Golgi apparatus membrane; Nucleus membrane | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- extracellular exosome (GO:0070062)
- extracellular space (GO:0005615)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 39 |
| PubMed broad count | 101 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: EVER2, EVIN2 |

**关键文献**:
1. Epidermodysplasia verruciformis.. *Current problems in dermatology*. PMID: 24643182
2. Recent advances in cutaneous HPV infection.. *The Journal of dermatology*. PMID: 36601717
3. Expression of a TMC6-TMC8-CIB1 heterotrimeric complex in lymphocytes is regulated by each of the components.. *The Journal of biological chemistry*. PMID: 32917726
4. Contribution of TMC6 and TMC8 (EVER1 and EVER2) variants to cervical cancer susceptibility.. *International journal of cancer*. PMID: 21387292
5. MmuPV1 infection of Tmc6/Ever1 or Tmc8/Ever2 deficient FVB mice as a model of βHPV in typical epidermodysplasia verruciformis.. *PLoS pathogens*. PMID: 39813296

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.9 |
| 高置信度残基 (pLDDT>90) 占比 | 26.9% |
| 置信残基 (pLDDT 70-90) 占比 | 48.6% |
| 中等置信 (pLDDT 50-70) 占比 | 9.9% |
| 低置信 (pLDDT<50) 占比 | 14.6% |
| 有序区域 (pLDDT>70) 占比 | 75.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=75.9，有序区 75.5%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038900, IPR012496; Pfam: PF07810 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SLC30A1 | 0.964 | 0.000 | — |
| SYNGR2 | 0.926 | 0.000 | — |
| TK1 | 0.750 | 0.000 | — |
| TMC6 | 0.740 | 0.000 | — |
| CANX | 0.730 | 0.070 | — |
| CIB1 | 0.717 | 0.109 | — |
| CORO1A | 0.662 | 0.089 | — |
| RHOH | 0.588 | 0.078 | — |
| DOCK8 | 0.571 | 0.050 | — |
| SASH3 | 0.549 | 0.045 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-2818167 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| bfmbAb | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A1Q4M0N4 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| H1-4 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.9 + PDB: 无 | pLDDT=75.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Golgi apparatus me / Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TMC8 — Transmembrane channel-like protein 8，非常新颖，仅有少数基础研究。
2. 蛋白大小726 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 39 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IU68
- Protein Atlas: https://www.proteinatlas.org/ENSG00000167895-TMC8/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TMC8
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IU68
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
