---
type: protein-evaluation
gene: "SRCAP"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SRCAP — REJECTED (研究热度过高 (PubMed strict=146，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SRCAP / KIAA0309 |
| 蛋白名称 | Chromatin remodeling protein SRCAP |
| 蛋白大小 | 3230 aa / 343.6 kDa |
| UniProt ID | Q6ZRS2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear bodies, Golgi apparatus; UniProt: Nucleus |
| 蛋白大小 | 0/10 | ×1 | 0 | 3230 aa / 343.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=146 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 6IGM, 8X15, 8X19, 8X1C, 9CA7, 9CA8, 9CA9 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR017956, IPR014001, IPR001650, IPR014012, IPR050 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **64.5/180** | |
| **归一化总分** | | | **35.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear bodies, Golgi apparatus | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Golgi apparatus (GO:0005794)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleosome (GO:0000786)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)
- protein-containing complex (GO:0032991)
- Swr1 complex (GO:0000812)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 146 |
| PubMed broad count | 227 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0309 |

**关键文献**:
1. SRCAP-Related Floating-Harbor Syndrome.. **. PMID: 23193612
2. Truncating SRCAP variants outside the Floating-Harbor syndrome locus cause a distinct neurodevelopmental disorder with a specific DNA methylation signature.. *American journal of human genetics*. PMID: 33909990
3. Colorectal cancer cell lines are representative models of the main molecular subtypes of primary cancer.. *Cancer research*. PMID: 24755471
4. Deficient H2A.Z deposition is associated with genesis of uterine leiomyoma.. *Nature*. PMID: 34349258
5. Genetic Findings in Short Turkish Children Born to Consanguineous Parents.. *Hormone research in paediatrics*. PMID: 38838658

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 6IGM, 8X15, 8X19, 8X1C, 9CA7, 9CA8, 9CA9, 9CAA, 9CAB |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017956, IPR014001, IPR001650, IPR014012, IPR050520; Pfam: PF00271, PF07529, PF00176 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RUVBL2 | 0.999 | 0.996 | — |
| ACTR6 | 0.999 | 0.996 | — |
| RUVBL1 | 0.999 | 0.996 | — |
| H2AZ1 | 0.998 | 0.943 | — |
| VPS72 | 0.997 | 0.932 | — |
| ZNHIT1 | 0.995 | 0.964 | — |
| DMAP1 | 0.992 | 0.958 | — |
| YEATS4 | 0.989 | 0.926 | — |
| KAT5 | 0.984 | 0.397 | — |
| CFDP1 | 0.970 | 0.882 | — |

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
| 三维结构 | AlphaFold pLDDT=0 + PDB: 6IGM, 8X15, 8X19, 8X1C, 9CA7,  | pLDDT=0, v? | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nuclear bodies, Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SRCAP — Chromatin remodeling protein SRCAP，研究基础较多，新颖性有限。
2. 蛋白大小3230 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 146 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 146 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ZRS2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000080603-SRCAP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SRCAP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ZRS2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
