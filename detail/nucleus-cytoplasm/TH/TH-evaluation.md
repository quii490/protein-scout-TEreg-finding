---
type: protein-evaluation
gene: "TH"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TH — REJECTED (研究热度过高 (PubMed strict=16111，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TH / TYH |
| 蛋白名称 | Tyrosine 3-monooxygenase |
| 蛋白大小 | 528 aa / 58.6 kDa |
| UniProt ID | P07101 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm, perinuclear region; Nucleus; Cell projection, axo |
| 蛋白大小 | 10/10 | ×1 | 10 | 528 aa / 58.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=16111 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=80.8; PDB: 2XSN, 4J6S, 6ZN2, 6ZVP, 6ZZU, 7A2G, 7PIM |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045865, IPR001273, IPR018301, IPR036951, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | Cytoplasm, perinuclear region; Nucleus; Cell projection, axon; Cytoplasm; Cytoplasmic vesicle, secre... | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- axon (GO:0030424)
- cytoplasm (GO:0005737)
- cytoplasmic side of plasma membrane (GO:0009898)
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- melanosome membrane (GO:0033162)
- neuron projection (GO:0043005)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16111 |
| PubMed broad count | 168129 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TYH |

**关键文献**:
1. Effects of electroacupuncture on mitophagy mediated by SIRT3/PINK1/Parkin pathway in Parkinson's disease mice.. *Zhen ci yan jiu = Acupuncture research*. PMID: 38500318
2. Inherited defects of thyroxine-binding proteins.. *Best practice & research. Clinical endocrinology & metabolism*. PMID: 26522458
3. [Tamm-Horsfall protein].. *Nephrologie*. PMID: 1579196
4. Thyroid hormone and cerebellar development.. *Cerebellum (London, England)*. PMID: 18418681
5. Segawa syndrome caused by TH gene mutation and its mechanism.. *Frontiers in genetics*. PMID: 36568392

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 80.8 |
| 高置信度残基 (pLDDT>90) 占比 | 57.4% |
| 置信残基 (pLDDT 70-90) 占比 | 19.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.6% |
| 低置信 (pLDDT<50) 占比 | 16.9% |
| 有序区域 (pLDDT>70) 占比 | 76.5% |
| 可用 PDB 条目 | 2XSN, 4J6S, 6ZN2, 6ZVP, 6ZZU, 7A2G, 7PIM |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2XSN, 4J6S, 6ZN2, 6ZVP, 6ZZU, 7A2G, 7PIM）+ AlphaFold极高置信度预测（pLDDT=80.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045865, IPR001273, IPR018301, IPR036951, IPR036329; Pfam: PF00351, PF21417, PF12549 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SNCA | 0.997 | 0.095 | — |
| DDC | 0.995 | 0.071 | — |
| PCBD1 | 0.987 | 0.000 | — |
| PCBD2 | 0.979 | 0.000 | — |
| DBH | 0.973 | 0.000 | — |
| QDPR | 0.972 | 0.000 | — |
| SPR | 0.969 | 0.000 | — |
| SLC18A2 | 0.966 | 0.095 | — |
| TYR | 0.963 | 0.045 | — |
| PNMT | 0.951 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000325951.4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| Dronc | psi-mi:"MI:0018"(two hybrid) | pubmed:10675329 |
| Diap1 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:10675329 |
| hid | psi-mi:"MI:0071"(molecular sieving) | pubmed:14517550 |
| eff | psi-mi:"MI:0096"(pull down) | pubmed:12021769 |
| rpr | psi-mi:"MI:0096"(pull down) | pubmed:12021769 |
| CG6911 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG4554 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| sina | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Tab2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=80.8 + PDB: 2XSN, 4J6S, 6ZN2, 6ZVP, 6ZZU,  | pLDDT=80.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, perinuclear region; Nucleus; Cell proje / Cytosol | 一致 |
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
1. TH — Tyrosine 3-monooxygenase，研究基础较多，新颖性有限。
2. 蛋白大小528 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16111 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 16111 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P07101
- Protein Atlas: https://www.proteinatlas.org/ENSG00000180176-TH/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TH
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P07101
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
