---
type: protein-evaluation
gene: "MAN1C1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MAN1C1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAN1C1 / MAN1A3, MAN1C |
| 蛋白名称 | Mannosyl-oligosaccharide 1,2-alpha-mannosidase IC |
| 蛋白大小 | 630 aa / 70.9 kDa |
| UniProt ID | Q9NR34 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Vesicles; UniProt: Golgi apparatus membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 630 aa / 70.9 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=28 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=82.1; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR012341, IPR001382, IPR050749, IPR036026; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **113.5/180** | |
| **归一化总分** | | | **63.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Vesicles | Uncertain |
| UniProt | Golgi apparatus membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- extracellular exosome (GO:0070062)
- Golgi membrane (GO:0000139)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 28 |
| PubMed broad count | 34 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: MAN1A3, MAN1C |

**关键文献**:
1. α-1,2-Mannosidase MAN1C1 Inhibits Proliferation and Invasion of Clear Cell Renal Cell Carcinoma.. *Journal of Cancer*. PMID: 30588245
2. Elevated α-1,2-mannosidase MAN1C1 in glioma stem cells and its implications for immunological changes and prognosis in glioma patients.. *Scientific reports*. PMID: 39333557
3. Potential drug targets for ovarian cancer identified through Mendelian randomization and colocalization analysis.. *Journal of ovarian research*. PMID: 39972314
4. Unique N-glycosylation signatures in human iPSC derived microglia activated by Aβ oligomer and lipopolysaccharide.. *Scientific reports*. PMID: 40210651
5. Hepatitis B virus upregulates host expression of α-1,2-mannosidases via the PPARα pathway.. *World journal of gastroenterology*. PMID: 27920474

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 82.1 |
| 高置信度残基 (pLDDT>90) 占比 | 68.3% |
| 置信残基 (pLDDT 70-90) 占比 | 7.0% |
| 中等置信 (pLDDT 50-70) 占比 | 3.7% |
| 低置信 (pLDDT<50) 占比 | 21.1% |
| 有序区域 (pLDDT>70) 占比 | 75.3% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=82.1，有序区 75.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012341, IPR001382, IPR050749, IPR036026; Pfam: PF01532 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAN1B1 | 0.941 | 0.000 | — |
| MGAT1 | 0.935 | 0.093 | — |
| MAN1A1 | 0.907 | 0.000 | — |
| MAN1A2 | 0.906 | 0.000 | — |
| MAN2A2 | 0.828 | 0.000 | — |
| MAN2A1 | 0.818 | 0.000 | — |
| COG2 | 0.611 | 0.000 | — |
| COG4 | 0.576 | 0.144 | — |
| GOLIM4 | 0.540 | 0.000 | — |
| COG5 | 0.537 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MYG1 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FARS2 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| FAM241A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| ENST00000374332 | psi-mi:"MI:2195"(clash) | pubmed:23622248|imex:IM-30030| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=82.1 + PDB: 无 | pLDDT=82.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Golgi apparatus membrane / Nucleoplasm, Vesicles | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

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
1. MAN1C1 — Mannosyl-oligosaccharide 1,2-alpha-mannosidase IC，非常新颖，仅有少数基础研究。
2. 蛋白大小630 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 28 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NR34
- Protein Atlas: https://www.proteinatlas.org/ENSG00000117643-MAN1C1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAN1C1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NR34
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
