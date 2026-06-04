---
type: protein-evaluation
gene: "WDR5"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## WDR5 — REJECTED (研究热度过高 (PubMed strict=442，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WDR5 / BIG3 |
| 蛋白名称 | WD repeat-containing protein 5 |
| 蛋白大小 | 334 aa / 36.6 kDa |
| UniProt ID | P61964 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Principal piece; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 334 aa / 36.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=442 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.3; PDB: 2CNX, 2CO0, 2G99, 2G9A, 2GNQ, 2H13, 2H14 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR059122, IPR015943, IPR020472, IPR019775, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Principal piece | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- ATAC complex (GO:0140672)
- histone acetyltransferase complex (GO:0000123)
- histone methyltransferase complex (GO:0035097)
- mitotic spindle (GO:0072686)
- MLL1 complex (GO:0071339)
- MLL1/2 complex (GO:0044665)
- MLL3/4 complex (GO:0044666)
- NSL complex (GO:0044545)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 442 |
| PubMed broad count | 602 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BIG3 |

**关键文献**:
1. Bidirectional histone monoaminylation dynamics regulate neural rhythmicity.. *Nature*. PMID: 39779849
2. STING mediates hepatocyte pyroptosis in liver fibrosis by Epigenetically activating the NLRP3 inflammasome.. *Redox biology*. PMID: 37018971
3. The glycolysis/HIF-1α axis defines the inflammatory role of IL-4-primed macrophages.. *Cell reports*. PMID: 37149865
4. Fibroblast-specific PRMT5 deficiency suppresses cardiac fibrosis and left ventricular dysfunction in male mice.. *Nature communications*. PMID: 38503742
5. MLL/WDR5 complex recruits centriolar satellite protein Cep72 to regulate microtubule nucleation and spindle formation.. *Science advances*. PMID: 39661677

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.3 |
| 高置信度残基 (pLDDT>90) 占比 | 89.2% |
| 置信残基 (pLDDT 70-90) 占比 | 1.8% |
| 中等置信 (pLDDT 50-70) 占比 | 1.5% |
| 低置信 (pLDDT<50) 占比 | 7.5% |
| 有序区域 (pLDDT>70) 占比 | 91.0% |
| 可用 PDB 条目 | 2CNX, 2CO0, 2G99, 2G9A, 2GNQ, 2H13, 2H14, 2H68, 2H6K, 2H6N |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2CNX, 2CO0, 2G99, 2G9A, 2GNQ, 2H13, 2H14, 2H68, 2H6K, 2H6N）+ AlphaFold极高置信度预测（pLDDT=93.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR059122, IPR015943, IPR020472, IPR019775, IPR036322; Pfam: PF25175 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| H3C12 | 0.999 | 0.972 | — |
| H3C13 | 0.999 | 0.915 | — |
| DPY30 | 0.999 | 0.970 | — |
| KANSL1 | 0.999 | 0.984 | — |
| RBBP5 | 0.999 | 0.998 | — |
| H3-3B | 0.999 | 0.915 | — |
| H3-4 | 0.999 | 0.980 | — |
| H3-2 | 0.999 | 0.915 | — |
| ASH2L | 0.999 | 0.995 | — |
| KMT2C | 0.999 | 0.983 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MBIP | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HCFC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12670868 |
| ATN1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| CUL4A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| RBBP5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| DTL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| SNRNP40 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| DDB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| GRWD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |
| CUL4B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17041588|imex:IM-19695 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.3 + PDB: 2CNX, 2CO0, 2G99, 2G9A, 2GNQ,  | pLDDT=93.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Principal piece | 一致 |
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
1. WDR5 — WD repeat-containing protein 5，研究基础较多，新颖性有限。
2. 蛋白大小334 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 442 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 442 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P61964
- Protein Atlas: https://www.proteinatlas.org/ENSG00000196363-WDR5/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WDR5
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P61964
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
