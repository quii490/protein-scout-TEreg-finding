---
type: protein-evaluation
gene: "CHUK"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CHUK — REJECTED (研究热度过高 (PubMed strict=118，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CHUK / IKKA, TCF16 |
| 蛋白名称 | Inhibitor of nuclear factor kappa-B kinase subunit alpha |
| 蛋白大小 | 745 aa / 84.6 kDa |
| UniProt ID | O15111 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 745 aa / 84.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=118 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=83.8; PDB: 3BRT, 5EBZ, 5TQW, 5TQX, 5TQY |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR041185, IPR046375, IPR051180, IPR022007, IPR011 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- CD40 receptor complex (GO:0035631)
- cytoplasm (GO:0005737)
- cytoplasmic side of plasma membrane (GO:0009898)
- cytosol (GO:0005829)
- IkappaB kinase complex (GO:0008385)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 118 |
| PubMed broad count | 1942 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: IKKA, TCF16 |

**关键文献**:
1. Multifaceted roles of TAX1BP1 in autophagy.. *Autophagy*. PMID: 35470757
2. New insights into the interplay between autophagy, gut microbiota and inflammatory responses in IBD.. *Autophagy*. PMID: 31286804
3. Role of AMBRA1 in mitophagy regulation: emerging evidence in aging-related diseases.. *Autophagy*. PMID: 39113560
4. Linear ubiquitination at damaged lysosomes induces local NFKB activation and controls cell survival.. *Autophagy*. PMID: 39744815
5. Inhibition of TRAF6 ubiquitin-ligase activity by PRDX1 leads to inhibition of NFKB activation and autophagy activation.. *Autophagy*. PMID: 29929436

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.8 |
| 高置信度残基 (pLDDT>90) 占比 | 59.2% |
| 置信残基 (pLDDT 70-90) 占比 | 23.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.4% |
| 低置信 (pLDDT<50) 占比 | 9.9% |
| 有序区域 (pLDDT>70) 占比 | 82.7% |
| 可用 PDB 条目 | 3BRT, 5EBZ, 5TQW, 5TQX, 5TQY |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3BRT, 5EBZ, 5TQW, 5TQX, 5TQY）+ AlphaFold极高置信度预测（pLDDT=83.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041185, IPR046375, IPR051180, IPR022007, IPR011009; Pfam: PF18397, PF12179, PF00069 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RELA | 0.999 | 0.880 | — |
| TNF | 0.999 | 0.994 | — |
| IKBKB | 0.999 | 0.994 | — |
| TRAF6 | 0.999 | 0.328 | — |
| NFKB1 | 0.999 | 0.854 | — |
| IRAK1 | 0.999 | 0.510 | — |
| NFKBIA | 0.999 | 0.994 | — |
| IKBKG | 0.999 | 0.994 | — |
| TNFRSF1A | 0.999 | 0.994 | — |
| TRAF3 | 0.998 | 0.090 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000359424.6 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| IKBKB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:9751060 |
| Trim44 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Sestd1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Krt10 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Arfip2 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Git1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Pex5 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Anxa13 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| Pbxip1 | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.8 + PDB: 3BRT, 5EBZ, 5TQW, 5TQX, 5TQY | pLDDT=83.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CHUK — Inhibitor of nuclear factor kappa-B kinase subunit alpha，研究基础较多，新颖性有限。
2. 蛋白大小745 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 118 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 118 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O15111
- Protein Atlas: https://www.proteinatlas.org/ENSG00000213341-CHUK/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CHUK
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O15111
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000213341-CHUK/subcellular

![](https://images.proteinatlas.org/1402/59_H6_3_red_green.jpg)
![](https://images.proteinatlas.org/1402/59_H6_4_red_green.jpg)
![](https://images.proteinatlas.org/1402/60_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/1402/60_H6_2_red_green.jpg)
![](https://images.proteinatlas.org/1402/61_H6_1_red_green.jpg)
![](https://images.proteinatlas.org/1402/61_H6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O15111-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
