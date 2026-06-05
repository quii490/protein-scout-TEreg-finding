---
type: protein-evaluation
gene: "NOPCHAP1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, recovery, re-evaluation]
status: scored
---

## NOPCHAP1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NOPCHAP1 / C12orf45 |
| 蛋白名称 | NOP protein chaperone 1 |
| 蛋白大小 | 185 aa / 20.1 kDa |
| UniProt ID | Q8N5I9 |
| 数据采集时间 | 2026-06-03 23:51:07 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | HPA: Nucleoplasm; 额外: Nuclear membrane; UniProt: Nucleus |
| 蛋白大小 | 8/10 | x1 | 8 | 185 aa / 20.1 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=1 篇 (<= 20 -> 10) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=70.3; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR027921; Pfam: PF15370 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **136.0/180** | |
| **归一化总分** | | | **75.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear membrane | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 1 |
| PubMed broad count | 2 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C12orf45 |

**关键文献**:
1. NOPCHAP1 is a PAQosome cofactor that helps loading NOP58 on RUVBL1/2 during box C/D snoRNP biogenesis.. *Nucleic acids research*. PMID: 33367824

**评价**: 极度新颖，几乎未被系统研究（PubMed <= 20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 70.3 |
| 高置信度残基 (pLDDT>90) 占比 | 13.0% |
| 置信残基 (pLDDT 70-90) 占比 | 29.7% |
| 中等置信 (pLDDT 50-70) 占比 | 49.2% |
| 低置信 (pLDDT<50) 占比 | 8.1% |
| 有序区域 (pLDDT>70) 占比 | 42.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=70.3，有序区 42.7%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR027921; Pfam: PF15370 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TBC1D23 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| BMX | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| SARS1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| SPAG1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| PRPF38A | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| CT55 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DNAJB6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| RUVBL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Ruvbl2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=70.3 + PDB: 无 | pLDDT=70.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. NOPCHAP1 -- NOP protein chaperone 1，极度新颖，几乎未被系统研究（PubMed <= 20篇）。
2. 蛋白大小185 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 1 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N5I9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000151131-NOPCHAP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NOPCHAP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N5I9
- STRING: https://string-db.org/network/9606.NOPCHAP1
- Packet data timestamp: 2026-06-03 23:51:07

---
*本报告为全量重评估 (Full Re-evaluation) -- Recovery from false-rejection。所有评分基于最新harvest packet数据，使用标准/180评分体系计算。*

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000151131-NOPCHAP1/subcellular

![](https://images.proteinatlas.org/38722/431_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/38722/431_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/38722/437_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/38722/437_A9_2_red_green.jpg)
![](https://images.proteinatlas.org/38722/443_A9_1_red_green.jpg)
![](https://images.proteinatlas.org/38722/443_A9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8N5I9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
