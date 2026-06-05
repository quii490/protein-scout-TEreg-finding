---
type: protein-evaluation
gene: "WDR49"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDR49 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WDR49 / WDR49 |
| 蛋白名称 | Cilia- and flagella-associated protein 337 |
| 蛋白大小 | 1049 aa / 119.0 kDa |
| UniProt ID | Q8IV35 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Nuclear bodies; 额外: Mitotic spindle, Primary ci; UniProt: Cell projection, cilium |
| 蛋白大小 | 8/10 | ×1 | 8 | 1049 aa / 119.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=71.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR011992, IPR002048, IPR051242, IPR015943, IPR020 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **119.5/180** | |
| **归一化总分** | | | **66.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Mitotic spindle, Primary cilium, Primary cilium tip, Primary cilium transition zone, Basal body, Cytosol | Approved |
| UniProt | Cell projection, cilium | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cilium (GO:0005929)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: WDR49 |

**关键文献**:
1. Genome-wide association study of the TP53 R249S mutation in hepatocellular carcinoma with aflatoxin B1 exposure and infection with hepatitis B virus.. *Journal of gastrointestinal oncology*. PMID: 33457005
2. An intrauterine genomic classifier reliably delineates the location of nonviable pregnancies.. *Fertility and sterility*. PMID: 33771330

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 71.9 |
| 高置信度残基 (pLDDT>90) 占比 | 26.6% |
| 置信残基 (pLDDT 70-90) 占比 | 40.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.9% |
| 低置信 (pLDDT<50) 占比 | 21.9% |
| 有序区域 (pLDDT>70) 占比 | 67.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=71.9，有序区 67.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011992, IPR002048, IPR051242, IPR015943, IPR020472; Pfam: PF00400 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SERPINI2 | 0.903 | 0.000 | — |
| ZBBX | 0.751 | 0.000 | — |
| GOLGA8F | 0.586 | 0.000 | — |
| TMEM253 | 0.583 | 0.000 | — |
| PLEKHH3 | 0.576 | 0.000 | — |
| LRRC74A | 0.573 | 0.000 | — |
| GOLGA8G | 0.549 | 0.000 | — |
| ARMCX2 | 0.529 | 0.000 | — |
| FAM124A | 0.513 | 0.000 | — |
| CROCC2 | 0.507 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CFAP337 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=71.9 + PDB: 无 | pLDDT=71.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium / Nucleoplasm, Nuclear bodies; 额外: Mitotic spindle,  | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

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
1. WDR49 — Cilia- and flagella-associated protein 337，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1049 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IV35
- Protein Atlas: https://www.proteinatlas.org/ENSG00000174776-WDR49/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WDR49
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IV35
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IV35-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000174776-WDR49/subcellular

![](https://images.proteinatlas.org/36226/2185_C7_50_blue_red_green.jpg)
![](https://images.proteinatlas.org/36226/2185_C7_66_blue_red_green.jpg)
![](https://images.proteinatlas.org/36226/2186_B6_44_blue_red_green.jpg)
![](https://images.proteinatlas.org/36226/2186_B6_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/36226/2242_D8_32_blue_red_green.jpg)
![](https://images.proteinatlas.org/36226/2242_D8_75_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
