---
type: protein-evaluation
gene: "EHF"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## EHF — REJECTED (研究热度过高 (PubMed strict=258，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EHF / ESE3, ESE3B, ESEJ |
| 蛋白名称 | ETS homologous factor |
| 蛋白大小 | 300 aa / 34.9 kDa |
| UniProt ID | Q9NZC4 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Golgi apparatus; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 300 aa / 34.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=258 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033071, IPR000418, IPR046328, IPR003118, IPR013 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 8 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Golgi apparatus | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- Golgi apparatus (GO:0005794)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 258 |
| PubMed broad count | 1313 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ESE3, ESE3B, ESEJ |

**关键文献**:
1. World Allergy Organization (WAO) Diagnosis and Rationale for Action against Cow's Milk Allergy (DRACMA) guideline update - XII - Recommendations on milk formula supplements with and without probiotics for infants and toddlers with CMA.. *The World Allergy Organization journal*. PMID: 38706757
2. European Headache Federation guideline on the use of monoclonal antibodies targeting the calcitonin gene related peptide pathway for migraine prevention - 2022 update.. *The journal of headache and pain*. PMID: 35690723
3. Hydrolysed Formulas in the Management of Cow's Milk Allergy: New Insights, Pitfalls and Tips.. *Nutrients*. PMID: 34444922
4. An Extensively Hydrolyzed Formula Supplemented with Two Human Milk Oligosaccharides Modifies the Fecal Microbiome and Metabolome in Infants with Cow's Milk Protein Allergy.. *International journal of molecular sciences*. PMID: 37511184
5. Integrative analysis of non-small cell lung cancer identifies Jumonji domain-containing 6/ETS homologous factor axis as a target to overcome radioresistance.. *Signal transduction and targeted therapy*. PMID: 41320721

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.9 |
| 高置信度残基 (pLDDT>90) 占比 | 27.7% |
| 置信残基 (pLDDT 70-90) 占比 | 25.7% |
| 中等置信 (pLDDT 50-70) 占比 | 7.0% |
| 低置信 (pLDDT<50) 占比 | 39.7% |
| 有序区域 (pLDDT>70) 占比 | 53.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.9），有序残基占 53.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033071, IPR000418, IPR046328, IPR003118, IPR013761; Pfam: PF00178, PF02198 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| APIP | 0.667 | 0.000 | — |
| ELF3 | 0.524 | 0.163 | — |
| KPRP | 0.471 | 0.471 | — |
| PDHX | 0.455 | 0.000 | — |
| TNFRSF1B | 0.426 | 0.422 | — |
| CST6 | 0.401 | 0.346 | — |
| PROM2 | 0.400 | 0.000 | — |
| SRSF1 | 0.400 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 8，IntAct interactions: 0
- 调控相关比例: 0 / 8 = 0%

**评价**: STRING 8 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.9 + PDB: 无 | pLDDT=67.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Golgi apparatus | 一致 |
| PPI | STRING + IntAct | 8 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. EHF — ETS homologous factor，研究基础较多，新颖性有限。
2. 蛋白大小300 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 258 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 258 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9NZC4
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135373-EHF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EHF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9NZC4
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
