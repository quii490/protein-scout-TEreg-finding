---
type: protein-evaluation
gene: "C14orf39"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C14orf39 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C14orf39 / C14orf39 |
| 蛋白名称 | Protein SIX6OS1 |
| 蛋白大小 | 587 aa / 68.2 kDa |
| UniProt ID | Q8N1H7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nucleoli; UniProt: Chromosome |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 587 aa / 68.2 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=9 篇 (≤20→10) |
| 🏗️ 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.0; PDB: 无 |
| 🧬 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031380; Pfam: PF15676 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 5 interactions |
| ➕ 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | Chromosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- central element (GO:0000801)
- chromosome (GO:0005694)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 9 |
| PubMed broad count | 15 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf39 |

**关键文献**:
1. Variations of C14ORF39 and SYCE1 Identified in Idiopathic Premature Ovarian Insufficiency and Nonobstructive Azoospermia.. *The Journal of clinical endocrinology and metabolism*. PMID: 34718620
2. Genetic variants in diminished ovarian reserve and premature ovarian insufficiency: implications for assisted reproductive outcomes.. *Journal of assisted reproduction and genetics*. PMID: 40936058
3. Genetic screening in patients with ovarian dysfunction.. *Clinical genetics*. PMID: 36373164
4. Homozygous mutations in C14orf39/SIX6OS1 cause non-obstructive azoospermia and premature ovarian insufficiency in humans.. *American journal of human genetics*. PMID: 33508233
5. C14ORF39/SIX6OS1 is a constituent of the synaptonemal complex and is essential for mouse fertility.. *Nature communications*. PMID: 27796301

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.0 |
| 高置信度残基 (pLDDT>90) 占比 | 27.9% |
| 置信残基 (pLDDT 70-90) 占比 | 10.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.1% |
| 低置信 (pLDDT<50) 占比 | 56.9% |
| 有序区域 (pLDDT>70) 占比 | 38.0% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=58.0），有序残基占 38.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031380; Pfam: PF15676 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SYCE2 | 0.886 | 0.000 | — |
| SYCE1 | 0.869 | 0.000 | — |
| TEX12 | 0.866 | 0.000 | — |
| SYCP1 | 0.829 | 0.000 | — |
| SYCE3 | 0.822 | 0.000 | — |
| SYCP3 | 0.600 | 0.045 | — |
| RNF212 | 0.581 | 0.000 | — |
| PSMA8 | 0.550 | 0.292 | — |
| MEIOB | 0.545 | 0.000 | — |
| SYCP2 | 0.544 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MT1X | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| HPGDS | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TEAD2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| TRIM54 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:31391242|imex:IM-25805| |
| SIX6OS1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 5
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 5 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.0 + PDB: 无 | pLDDT=58.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Chromosome / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 5 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. C14orf39 — Protein SIX6OS1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小587 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 9 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=58.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8N1H7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000179008-C14orf39/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C14orf39
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8N1H7
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:21:06

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000179008-C14orf39/subcellular

![](https://images.proteinatlas.org/59518/1385_C6_1_red_green.jpg)
![](https://images.proteinatlas.org/59518/1385_C6_2_red_green.jpg)
![](https://images.proteinatlas.org/59518/1394_C6_4_red_green.jpg)
![](https://images.proteinatlas.org/59518/1394_C6_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
