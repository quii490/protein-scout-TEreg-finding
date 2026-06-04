---
type: protein-evaluation
gene: "IMPACT"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## IMPACT — REJECTED (研究热度过高 (PubMed strict=210549，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | IMPACT |
| 蛋白名称 | Protein IMPACT |
| 蛋白大小 | 320 aa / 36.5 kDa |
| UniProt ID | Q9P2X3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 320 aa / 36.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=210549 篇 (>100→REJECTED) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=80.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR023582, IPR001498, IPR036956, IPR020568, IPR006 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **73.5/180** | |
| **归一化总分** | | | **40.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Approved |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 210549 |
| PubMed broad count | 1921700 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Ketogenesis impact on liver metabolism revealed by proteomics of lysine β-hydroxybutyrylation.. *Cell reports*. PMID: 34348140
2. PNPLA3(148M) is a gain-of-function mutation that promotes hepatic steatosis by inhibiting ATGL-mediated triglyceride hydrolysis.. *Journal of hepatology*. PMID: 39550037
3. Mutational scanning pinpoints distinct binding sites of key ATGL regulators in lipolysis.. *Nature communications*. PMID: 38514628
4. Nutrient-Dependent Changes of Protein Palmitoylation: Impact on Nuclear Enzymes and Regulation of Gene Expression.. *International journal of molecular sciences*. PMID: 30513609
5. The physiological impact of microRNA gene regulation in the retina.. *Cellular and molecular life sciences : CMLS*. PMID: 22460583

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.2 |
| 高置信度残基 (pLDDT>90) 占比 | 59.7% |
| 置信残基 (pLDDT 70-90) 占比 | 15.9% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 21.9% |
| 有序区域 (pLDDT>70) 占比 | 75.6% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=80.2，有序区 75.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023582, IPR001498, IPR036956, IPR020568, IPR006575; Pfam: PF01205, PF05773 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GRHPR | 0.849 | 0.000 | — |
| TK1 | 0.816 | 0.000 | — |
| CMPK2 | 0.809 | 0.000 | — |
| DTYMK | 0.809 | 0.000 | — |
| DHFR2 | 0.795 | 0.000 | — |
| DHFR | 0.793 | 0.000 | — |
| CTBP2 | 0.702 | 0.000 | — |
| PHGDH | 0.687 | 0.000 | — |
| CTBP1 | 0.687 | 0.000 | — |
| GCN1 | 0.668 | 0.313 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-2844490 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| PSMB1 | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| SERPINF1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| CA10 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CRHBP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| Map3k1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| UBE2V1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| UBA1 | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| UBE2N | psi-mi:"MI:0997"(ubiquitinase assay) | imex:IM-22822|pubmed:25260751 |
| Pafah1b1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26496610|imex:IM-24272 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.2 + PDB: 无 | pLDDT=80.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. IMPACT — Protein IMPACT，研究基础较多，新颖性有限。
2. 蛋白大小320 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 210549 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 210549 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9P2X3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000154059-IMPACT/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=IMPACT
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9P2X3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
