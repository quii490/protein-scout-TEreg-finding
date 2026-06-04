---
type: protein-evaluation
gene: "FAM89A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FAM89A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FAM89A / C1orf153 |
| 蛋白名称 | Protein FAM89A |
| 蛋白大小 | 184 aa / 19.6 kDa |
| UniProt ID | Q96GI7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Golgi apparatus, Vesicles; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 184 aa / 19.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=66.0; PDB: 无 |
| 调控结构域 | 5/10 | ×2 | 10 | 无注释结构域 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Golgi apparatus, Vesicles; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 12 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C1orf153 |

**关键文献**:
1. Uncovering hub genes in sepsis through bioinformatics analysis.. *Medicine*. PMID: 38050254
2. FAM89A and IFI44L for distinguishing between viral and bacterial infections in children with febrile illness.. *Pediatric investigation*. PMID: 34589675
3. Pilot genome-wide association study of antibody response to inactivated SARS-CoV-2 vaccines.. *Frontiers in immunology*. PMID: 36451823
4. Comparative proteomic approach in rat model of absence epilepsy.. *Journal of molecular neuroscience : MN*. PMID: 25323782
5. Transcriptome-wide association study reveals two genes that influence mismatch negativity.. *Cell reports*. PMID: 33730571

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 66.0 |
| 高置信度残基 (pLDDT>90) 占比 | 21.7% |
| 置信残基 (pLDDT 70-90) 占比 | 14.7% |
| 中等置信 (pLDDT 50-70) 占比 | 34.8% |
| 低置信 (pLDDT<50) 占比 | 28.8% |
| 有序区域 (pLDDT>70) 占比 | 36.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=66.0），有序残基占 36.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | 无注释结构域 |

**染色质调控潜力分析**: 结构域注释有限，AlphaFold预测有可辨识折叠域。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ANAPC5 | 0.848 | 0.789 | — |
| ANAPC1 | 0.848 | 0.789 | — |
| CDC16 | 0.845 | 0.785 | — |
| ANAPC4 | 0.840 | 0.777 | — |
| ANAPC2 | 0.840 | 0.777 | — |
| CDC23 | 0.830 | 0.769 | — |
| HSPB11 | 0.661 | 0.573 | — |
| ANAPC10 | 0.661 | 0.573 | — |
| CDC42BPB | 0.622 | 0.622 | — |
| CDC27 | 0.594 | 0.440 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBXN2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HCN1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:37207277|imex:IM-29810 |
| ECE1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-30316|pubmed:38413612| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=66.0 + PDB: 无 | pLDDT=66.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Golgi apparatus, Vesicles; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. FAM89A — Protein FAM89A，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小184 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=66.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96GI7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182118-FAM89A/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FAM89A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96GI7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
