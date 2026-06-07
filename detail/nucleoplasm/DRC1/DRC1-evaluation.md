---
type: protein-evaluation
gene: "DRC1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DRC1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DRC1 / C2orf39, CCDC164 |
| 蛋白名称 | Dynein regulatory complex protein 1 |
| 蛋白大小 | 740 aa / 87.1 kDa |
| UniProt ID | Q96MC2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Primary cilium transition zone; UniProt: Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm, cytoskel |
| 蛋白大小 | 10/10 | ×1 | 10 | 740 aa / 87.1 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=59 篇 (≤60→6) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=74.8; PDB: 8J07 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR039505, IPR039750, IPR029440; Pfam: PF14772, PF |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **104.5/180** | |
| **归一化总分** | | | **58.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Primary cilium transition zone | Approved |
| UniProt | Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm, cytoskeleton, flagellum axoneme | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- axonemal dynein complex (GO:0005858)
- axoneme (GO:0005930)
- cytosol (GO:0005829)
- extracellular region (GO:0005576)
- sperm flagellum (GO:0036126)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 59 |
| PubMed broad count | 135 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C2orf39, CCDC164 |

**关键文献**:
1. Primary Ciliary Dyskinesia.. **. PMID: 20301301
2. A 3000-year-old founder variant in the DRC1 gene causes primary ciliary dyskinesia in Japan and Korea.. *Journal of human genetics*. PMID: 39152285
3. DRC1, DNA replication and checkpoint protein 1, functions with DPB11 to control DNA replication and the S-phase checkpoint in Saccharomyces cerevisiae.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 10097122
4. A case of primary ciliary dyskinesis with DRC1 deletion and literature review: Additional evidence on the founder effect.. *Pediatrics international : official journal of the Japan Pediatric Society*. PMID: 39349394
5. Characterization of a DRC1 null variant associated with primary ciliary dyskinesia and female infertility.. *Journal of assisted reproduction and genetics*. PMID: 36856967

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.8 |
| 高置信度残基 (pLDDT>90) 占比 | 33.2% |
| 置信残基 (pLDDT 70-90) 占比 | 38.0% |
| 中等置信 (pLDDT 50-70) 占比 | 10.5% |
| 低置信 (pLDDT<50) 占比 | 18.2% |
| 有序区域 (pLDDT>70) 占比 | 71.2% |
| 可用 PDB 条目 | 8J07 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=74.8，有序区 71.2%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039505, IPR039750, IPR029440; Pfam: PF14772, PF14775 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CCDC65 | 0.940 | 0.000 | — |
| GAS8 | 0.896 | 0.000 | — |
| CCDC40 | 0.884 | 0.000 | — |
| CCDC39 | 0.874 | 0.050 | — |
| DRC7 | 0.860 | 0.000 | — |
| CCDC103 | 0.855 | 0.000 | — |
| DNAI1 | 0.827 | 0.000 | — |
| CCDC114 | 0.823 | 0.000 | — |
| DNAI2 | 0.818 | 0.000 | — |
| RSPH9 | 0.808 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 3 / 15 = 20%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.8 + PDB: 8J07 | pLDDT=74.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton, cilium axoneme; Cytoplasm / Nucleoplasm, Primary cilium transition zone | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DRC1 — Dynein regulatory complex protein 1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小740 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 59 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96MC2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157856-DRC1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DRC1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96MC2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000157856-DRC1/subcellular

![](https://images.proteinatlas.org/51247/2204_C2_20_blue_red_green.jpg)
![](https://images.proteinatlas.org/51247/2204_C2_8_blue_red_green.jpg)
![](https://images.proteinatlas.org/51247/2234_F2_36_blue_red_green.jpg)
![](https://images.proteinatlas.org/51247/2234_F2_80_blue_red_green.jpg)
![](https://images.proteinatlas.org/51247/2241_G2_40_blue_red_green.jpg)
![](https://images.proteinatlas.org/51247/2241_G2_64_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96MC2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96MC2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR039505;IPR039750;IPR029440; |
| Pfam | PF14772;PF14775; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000157856-DRC1/interaction

未从 HPA Interaction 页面解析到互作伙伴；需人工复核或使用其他 humanPPI 来源。
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
