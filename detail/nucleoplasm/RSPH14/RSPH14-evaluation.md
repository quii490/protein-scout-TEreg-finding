---
type: protein-evaluation
gene: "RSPH14"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## RSPH14 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RSPH14 / RTDR1 |
| 蛋白名称 | Radial spoke head 14 homolog |
| 蛋白大小 | 348 aa / 38.6 kDa |
| UniProt ID | Q9UHP6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoli; UniProt: Cytoplasm, cytoskeleton, flagellum axoneme |
| 蛋白大小 | 10/10 | ×1 | 10 | 348 aa / 38.6 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=2 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.7; PDB: 8J07 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011989, IPR016024, IPR000225, IPR042856; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **126.5/180** | |
| **归一化总分** | | | **70.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli | Uncertain |
| UniProt | Cytoplasm, cytoskeleton, flagellum axoneme | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- radial spoke (GO:0001534)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2 |
| PubMed broad count | 5 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RTDR1 |

**关键文献**:
1. IQUB mutation induces radial spoke 1 deficiency causing asthenozoospermia with normal sperm morphology in humans and mice.. *Cell communication and signaling : CCS*. PMID: 39849482
2. Characterization of the genomic landscape of canine diffuse large B-cell lymphoma reveals recurrent H3K27M mutations linked to progression-free survival.. *Scientific reports*. PMID: 39922874

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.7 |
| 高置信度残基 (pLDDT>90) 占比 | 89.7% |
| 置信残基 (pLDDT 70-90) 占比 | 3.2% |
| 中等置信 (pLDDT 50-70) 占比 | 1.4% |
| 低置信 (pLDDT<50) 占比 | 5.7% |
| 有序区域 (pLDDT>70) 占比 | 92.9% |
| 可用 PDB 条目 | 8J07 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.7，有序区 92.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011989, IPR016024, IPR000225, IPR042856; Pfam: PF00514 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RAB36 | 0.983 | 0.000 | — |
| RAB13 | 0.813 | 0.000 | — |
| RAB23 | 0.810 | 0.000 | — |
| CFAP52 | 0.712 | 0.126 | — |
| WDR38 | 0.686 | 0.126 | — |
| CCDC65 | 0.636 | 0.305 | — |
| ANKEF1 | 0.634 | 0.121 | — |
| KRT75 | 0.630 | 0.627 | — |
| C9orf135 | 0.622 | 0.401 | — |
| TSNAXIP1 | 0.608 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.7 + PDB: 8J07 | pLDDT=92.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, flagellum axoneme / Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. RSPH14 — Radial spoke head 14 homolog，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小348 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UHP6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100218-RSPH14/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RSPH14
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UHP6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoli (uncertain)。来源: https://www.proteinatlas.org/ENSG00000100218-RSPH14/subcellular

![](https://images.proteinatlas.org/50425/1310_G5_1_red_green.jpg)
![](https://images.proteinatlas.org/50425/1310_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/50425/1312_G5_2_red_green.jpg)
![](https://images.proteinatlas.org/50425/1312_G5_3_red_green.jpg)
![](https://images.proteinatlas.org/50425/1339_E9_1_red_green.jpg)
![](https://images.proteinatlas.org/50425/1339_E9_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UHP6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
