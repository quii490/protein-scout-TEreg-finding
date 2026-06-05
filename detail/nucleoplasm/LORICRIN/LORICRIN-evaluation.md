---
type: protein-evaluation
gene: "LORICRIN"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LORICRIN — REJECTED (研究热度过高 (PubMed strict=538，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LORICRIN / LOR, LRN |
| 蛋白名称 | Loricrin |
| 蛋白大小 | 312 aa / 25.8 kDa |
| UniProt ID | P23490 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus, nucleoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 312 aa / 25.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=538 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=43.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR031700; Pfam: PF15847 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.0/180** | |
| **归一化总分** | | | **44.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cornified envelope (GO:0001533)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 538 |
| PubMed broad count | 953 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LOR, LRN |

**关键文献**:
1. Autophagy-based unconventional secretion of HMGB1 by keratinocytes plays a pivotal role in psoriatic skin inﬂammation.. *Autophagy*. PMID: 32019420
2. Abrocitinib versus dupilumab: Impact on skin barrier function and proteomics in atopic dermatitis.. *Journal of the American Academy of Dermatology*. PMID: 40246083
3. Targeting IL-13 with tralokinumab normalizes type 2 inflammation in atopic dermatitis both early and at 2 years.. *Allergy*. PMID: 38563683
4. Palmoplantar keratodermas.. *Clinics in dermatology*. PMID: 15708285
5. Eisenia bicyclis Extract Repairs UVB-Induced Skin Photoaging In Vitro and In Vivo: Photoprotective Effects.. *Marine drugs*. PMID: 34940692

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 43.1 |
| 高置信度残基 (pLDDT>90) 占比 | 0.0% |
| 置信残基 (pLDDT 70-90) 占比 | 9.0% |
| 中等置信 (pLDDT 50-70) 占比 | 8.3% |
| 低置信 (pLDDT<50) 占比 | 82.7% |
| 有序区域 (pLDDT>70) 占比 | 9.0% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=43.1），有序残基占 9.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR031700; Pfam: PF15847 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| IVL | 0.999 | 0.292 | — |
| FLG2 | 0.999 | 0.000 | — |
| FLG | 0.998 | 0.000 | — |
| TCHH | 0.989 | 0.000 | — |
| KRT1 | 0.953 | 0.292 | — |
| KRT10 | 0.948 | 0.000 | — |
| TGM1 | 0.933 | 0.000 | — |
| CDSN | 0.933 | 0.000 | — |
| SPRR3 | 0.930 | 0.000 | — |
| SPRR1B | 0.928 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| VIM | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| - | psi-mi:"MI:0096"(pull down) | pubmed:31964889|imex:IM-27520 |
| ZDHHC23 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ZSCAN12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| B3GALNT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Xpo1 | psi-mi:"MI:0096"(pull down) | pubmed:26673895|imex:IM-24970 |
| CCNC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NDUFS5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| AAAS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ZNF550 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=43.1 + PDB: 无 | pLDDT=43.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleoplasm / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. LORICRIN — Loricrin，研究基础较多，新颖性有限。
2. 蛋白大小312 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 538 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=43.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 538 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P23490
- Protein Atlas: https://www.proteinatlas.org/ENSG00000203782-LORICRIN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LORICRIN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P23490
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P23490-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
