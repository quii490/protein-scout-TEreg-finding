---
type: protein-evaluation
gene: "WEE2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WEE2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WEE2 / WEE1B |
| 蛋白名称 | Wee1-like protein kinase 2 |
| 蛋白大小 | 567 aa / 62.9 kDa |
| UniProt ID | P0C1S8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 567 aa / 62.9 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=60 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.1; PDB: 5VDK |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR050339, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **110.0/180** | |
| **归一化总分** | | | **61.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- plasma membrane (GO:0005886)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 60 |
| PubMed broad count | 81 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: WEE1B |

**关键文献**:
1. Total fertilization failure after ICSI: insights into pathophysiology, diagnosis, and management through artificial oocyte activation.. *Human reproduction update*. PMID: 36977357
2. Genetic factors as potential molecular markers of human oocyte and embryo quality.. *Journal of assisted reproduction and genetics*. PMID: 33895934
3. Oocyte-specific Wee1-like protein kinase 2 is dispensable for fertility in mice.. *PloS one*. PMID: 37527245
4. Novel splicing mutations in PATL2 and WEE2 cause oocyte degradation and fertilization failure.. *Journal of assisted reproduction and genetics*. PMID: 39476306
5. Novel WEE2 gene variants identified in patients with fertilization failure and female infertility.. *Fertility and sterility*. PMID: 30827524

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.1 |
| 高置信度残基 (pLDDT>90) 占比 | 40.2% |
| 置信残基 (pLDDT 70-90) 占比 | 9.3% |
| 中等置信 (pLDDT 50-70) 占比 | 9.5% |
| 低置信 (pLDDT<50) 占比 | 40.9% |
| 有序区域 (pLDDT>70) 占比 | 49.5% |
| 可用 PDB 条目 | 5VDK |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.1），有序残基占 49.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR050339, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CHEK1 | 0.955 | 0.300 | — |
| CDK1 | 0.953 | 0.314 | — |
| WEE1 | 0.909 | 0.000 | — |
| CHEK2 | 0.838 | 0.767 | — |
| CDC25B | 0.788 | 0.474 | — |
| CKAP5 | 0.782 | 0.782 | — |
| PATL2 | 0.715 | 0.000 | — |
| CDC25A | 0.702 | 0.474 | — |
| CDC25C | 0.675 | 0.474 | — |
| CCNB1 | 0.657 | 0.310 | — |

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
| 三维结构 | AlphaFold pLDDT=67.1 + PDB: 5VDK | pLDDT=67.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. WEE2 — Wee1-like protein kinase 2，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小567 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 60 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=67.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P0C1S8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000214102-WEE2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WEE2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P0C1S8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
