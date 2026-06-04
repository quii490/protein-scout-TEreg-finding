---
type: protein-evaluation
gene: "NDRG2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NDRG2 — REJECTED (研究热度过高 (PubMed strict=403，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NDRG2 / KIAA1248, SYLD |
| 蛋白名称 | Protein NDRG2 |
| 蛋白大小 | 371 aa / 40.8 kDa |
| UniProt ID | Q9UN36 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Centriolar satellite; 额外: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Cytoplasm, perinuclear region; Cell projection, g |
| 蛋白大小 | 10/10 | ×1 | 10 | 371 aa / 40.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=403 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=83.6; PDB: 2XMQ, 2XMR, 2XMS |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029058, IPR004142; Pfam: PF03096 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 10 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.0/180** | |
| **归一化总分** | | | **51.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centriolar satellite; 额外: Nucleoplasm, Cytosol | Approved |
| UniProt | Cytoplasm; Cytoplasm, perinuclear region; Cell projection, growth cone | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- Golgi apparatus (GO:0005794)
- growth cone (GO:0030426)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 403 |
| PubMed broad count | 452 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1248, SYLD |

**关键文献**:
1. Astrocytic NDRG2-PPM1A interaction exacerbates blood-brain barrier disruption after subarachnoid hemorrhage.. *Science advances*. PMID: 36179025
2. Reprogramming astrocytic NDRG2/NF-κB/C3 signaling restores the diabetes-associated cognitive dysfunction.. *EBioMedicine*. PMID: 37329577
3. Integrative eQTL and Mendelian randomization analysis reveals key genetic markers in mesothelioma.. *Respiratory research*. PMID: 40223054
4. ROS promote hyper-methylation of NDRG2 promoters in a DNMTS-dependent manner: Contributes to the progression of renal fibrosis.. *Redox biology*. PMID: 36989575
5. Astrocyte-specific NDRG2 gene: functions in the brain and neurological diseases.. *Cellular and molecular life sciences : CMLS*. PMID: 31834421

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.6 |
| 高置信度残基 (pLDDT>90) 占比 | 69.3% |
| 置信残基 (pLDDT 70-90) 占比 | 11.1% |
| 中等置信 (pLDDT 50-70) 占比 | 3.8% |
| 低置信 (pLDDT<50) 占比 | 15.9% |
| 有序区域 (pLDDT>70) 占比 | 80.4% |
| 可用 PDB 条目 | 2XMQ, 2XMR, 2XMS |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2XMQ, 2XMR, 2XMS）+ AlphaFold高质量预测（pLDDT=83.6），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029058, IPR004142; Pfam: PF03096 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| STK38L | 0.929 | 0.000 | — |
| MYCN | 0.868 | 0.000 | — |
| NDRG1 | 0.800 | 0.785 | — |
| CTNNB1 | 0.495 | 0.348 | — |
| MAPT | 0.465 | 0.320 | — |
| TRIM32 | 0.441 | 0.292 | — |
| SNAI1 | 0.441 | 0.292 | — |
| NF2 | 0.432 | 0.000 | — |
| GFAP | 0.413 | 0.000 | — |
| WSB1 | 0.404 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDK15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DDX19B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| NDRG1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CCR1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| NRSN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SSUH2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| RNF115 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SSBP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| PPP2R2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 10，IntAct interactions: 15
- 调控相关比例: 0 / 10 = 0%

**评价**: STRING 10 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.6 + PDB: 2XMQ, 2XMR, 2XMS | pLDDT=83.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasm, perinuclear region; Cell pro / Centriolar satellite; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 10 + 15 interactions | 数据充分 |

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
1. NDRG2 — Protein NDRG2，研究基础较多，新颖性有限。
2. 蛋白大小371 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 403 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 403 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UN36
- Protein Atlas: https://www.proteinatlas.org/ENSG00000165795-NDRG2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NDRG2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UN36
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
