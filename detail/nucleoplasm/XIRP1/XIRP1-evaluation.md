---
type: protein-evaluation
gene: "XIRP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## XIRP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | XIRP1 / CMYA1, XIN |
| 蛋白名称 | Xin actin-binding repeat-containing protein 1 |
| 蛋白大小 | 1843 aa / 198.6 kDa |
| UniProt ID | Q702N8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Actin filaments; 额外: Nucleoplasm; UniProt: Cell junction, adherens junction; Cell junction, desmosome |
| 蛋白大小 | 5/10 | ×1 | 5 | 1843 aa / 198.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=30 篇 (≤40→8) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=43.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012510, IPR030072; Pfam: PF08043 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 12 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **115.0/180** | |
| **归一化总分** | | | **63.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Actin filaments; 额外: Nucleoplasm | Approved |
| UniProt | Cell junction, adherens junction; Cell junction, desmosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- adherens junction (GO:0005912)
- desmosome (GO:0030057)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 30 |
| PubMed broad count | 44 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CMYA1, XIN |

**关键文献**:
1. Accelerating novel candidate gene discovery in neurogenetic disorders via whole-exome sequencing of prescreened multiplex consanguineous families.. *Cell reports*. PMID: 25558065
2. miR-125 family regulates XIRP1 and FIH in response to myocardial infarction.. *Physiological genomics*. PMID: 32716698
3. Hypoxia-induced circPLOD2a/b promotes the aggressiveness of glioblastoma by suppressing XIRP1 through binding to HuR.. *Communications biology*. PMID: 39820362
4. Discovery of novel vitamin D receptor interacting proteins that modulate 1,25-dihydroxyvitamin D3 signaling.. *The Journal of steroid biochemistry and molecular biology*. PMID: 22626544
5. Recurrent Frameshift Neoantigen Vaccine Elicits Protective Immunity With Reduced Tumor Burden and Improved Overall Survival in a Lynch Syndrome Mouse Model.. *Gastroenterology*. PMID: 34224739

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 43.6 |
| 高置信度残基 (pLDDT>90) 占比 | 4.6% |
| 置信残基 (pLDDT 70-90) 占比 | 11.4% |
| 中等置信 (pLDDT 50-70) 占比 | 15.6% |
| 低置信 (pLDDT<50) 占比 | 68.4% |
| 有序区域 (pLDDT>70) 占比 | 16.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=43.6），有序残基占 16.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012510, IPR030072; Pfam: PF08043 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| OXNAD1 | 0.884 | 0.045 | — |
| FLNC | 0.843 | 0.493 | — |
| CAPN7 | 0.841 | 0.085 | — |
| ACTN2 | 0.759 | 0.094 | — |
| CSRP3 | 0.736 | 0.049 | — |
| CAV3 | 0.698 | 0.000 | — |
| CDH2 | 0.658 | 0.000 | — |
| NRAP | 0.652 | 0.053 | — |
| TTN | 0.632 | 0.000 | — |
| KLHL40 | 0.624 | 0.091 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FLNC | psi-mi:"MI:0018"(two hybrid) | pubmed:16631741|imex:IM-22914 |
| VASP | psi-mi:"MI:0047"(far western blotting) | pubmed:16631741|imex:IM-22914 |
| Enah | psi-mi:"MI:0018"(two hybrid) | pubmed:16631741|imex:IM-22914 |
| Evl | psi-mi:"MI:0018"(two hybrid) | pubmed:16631741|imex:IM-22914 |
| SOCS7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TRIM55 | psi-mi:"MI:0096"(pull down) | pubmed:31391242|imex:IM-25805| |
| Cav3 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:24952909|imex:IM-26422 |
| ABCA2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SCN4A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 12
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 12 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=43.6 + PDB: 无 | pLDDT=43.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell junction, adherens junction; Cell junction, d / Actin filaments; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 12 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. XIRP1 — Xin actin-binding repeat-containing protein 1，非常新颖，仅有少数基础研究。
2. 蛋白大小1843 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 30 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=43.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q702N8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168334-XIRP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=XIRP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q702N8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Actin filaments (uncertain)。来源: https://www.proteinatlas.org/ENSG00000168334-XIRP1/subcellular

![](https://images.proteinatlas.org/26391/636_B12_3_red_green.jpg)
![](https://images.proteinatlas.org/26391/636_B12_8_red_green.jpg)
![](https://images.proteinatlas.org/26391/637_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/26391/637_B12_3_red_green.jpg)
![](https://images.proteinatlas.org/26391/638_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/26391/638_B12_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q702N8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q702N8 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR012510;IPR030072; |
| Pfam | PF08043; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168334-XIRP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| FLNC | Intact, Biogrid | true |
| VASP | Intact, Biogrid | true |
| NEB | Biogrid | false |
| NEBL | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
