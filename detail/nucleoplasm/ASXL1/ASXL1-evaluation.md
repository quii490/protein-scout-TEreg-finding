---
type: protein-evaluation
gene: "ASXL1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ASXL1 — REJECTED (研究热度过高 (PubMed strict=861，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ASXL1 / KIAA0978 |
| 蛋白名称 | Polycomb group protein ASXL1 |
| 蛋白大小 | 1541 aa / 165.4 kDa |
| UniProt ID | Q8IXJ9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm, Nucleoli; UniProt: Nucleus |
| 蛋白大小 | 5/10 | ×1 | 5 | 1541 aa / 165.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=861 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=42.2; PDB: 8H1T, 8SVF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR026905, IPR024811, IPR028020, IPR007759, IPR044 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **83.0/180** | |
| **归一化总分** | | | **46.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nucleoli | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- nucleoplasm (GO:0005654)
- PR-DUB complex (GO:0035517)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 861 |
| PubMed broad count | 1898 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0978 |

**关键文献**:
1. Chronic neutrophilic leukemia preceded by myelodysplastic syndromes.. *International journal of hematology*. PMID: 37439996
2. Genomics of myelodysplastic syndrome/myeloproliferative neoplasm overlap syndromes.. *Hematology. American Society of Hematology. Education Program*. PMID: 33275756
3. Bohring-Opitz Syndrome.. **. PMID: 29446906
4. Chronic myelomonocytic leukemia: 2022 update on diagnosis, risk stratification, and management.. *American journal of hematology*. PMID: 34985762
5. Inherited resilience to clonal hematopoiesis by modifying stem cell RNA regulation.. *Science (New York, N.Y.)*. PMID: 41477881

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 42.2 |
| 高置信度残基 (pLDDT>90) 占比 | 3.4% |
| 置信残基 (pLDDT 70-90) 占比 | 9.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.0% |
| 低置信 (pLDDT<50) 占比 | 81.5% |
| 有序区域 (pLDDT>70) 占比 | 12.5% |
| 可用 PDB 条目 | 8H1T, 8SVF |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=42.2），有序残基占 12.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026905, IPR024811, IPR028020, IPR007759, IPR044867; Pfam: PF13919, PF05066, PF13922 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BAP1 | 0.999 | 0.922 | — |
| EZH2 | 0.998 | 0.314 | — |
| SUZ12 | 0.995 | 0.292 | — |
| FOXK1 | 0.987 | 0.698 | — |
| OGT | 0.982 | 0.598 | — |
| TET2 | 0.975 | 0.000 | — |
| RBBP4 | 0.973 | 0.331 | — |
| HCFC1 | 0.967 | 0.679 | — |
| RNF2 | 0.945 | 0.306 | — |
| BMI1 | 0.944 | 0.300 | — |

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
| 三维结构 | AlphaFold pLDDT=42.2 + PDB: 8H1T, 8SVF | pLDDT=42.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nucleoli | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. ASXL1 — Polycomb group protein ASXL1，研究基础较多，新颖性有限。
2. 蛋白大小1541 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 861 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=42.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 861 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IXJ9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171456-ASXL1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ASXL1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IXJ9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
