---
type: protein-evaluation
gene: "MYB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MYB — REJECTED (研究热度过高 (PubMed strict=8049，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MYB |
| 蛋白名称 | Transcriptional activator Myb |
| 蛋白大小 | 640 aa / 72.3 kDa |
| UniProt ID | P10242 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 640 aa / 72.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=8049 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR015395, IPR009057, IPR017930, IPR050560, IPR001 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nuclear matrix (GO:0016363)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 8049 |
| PubMed broad count | 11411 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The R2R3-MYB gene family in Arabidopsis thaliana.. *Current opinion in plant biology*. PMID: 11597504
2. Genome-wide identification and expression analysis of the R2R3-MYB gene family in tobacco (Nicotiana tabacum L.).. *BMC genomics*. PMID: 35681121
3. Ki-67 gene expression.. *Cell death and differentiation*. PMID: 34183782
4. The MYB transcription factor superfamily of Arabidopsis: expression analysis and phylogenetic comparison with the rice MYB family.. *Plant molecular biology*. PMID: 16463103
5. c-MYB and DMTF1 in Cancer.. *Cancer investigation*. PMID: 30599775

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.1 |
| 高置信度残基 (pLDDT>90) 占比 | 23.3% |
| 置信残基 (pLDDT 70-90) 占比 | 7.2% |
| 中等置信 (pLDDT 50-70) 占比 | 12.0% |
| 低置信 (pLDDT<50) 占比 | 57.5% |
| 有序区域 (pLDDT>70) 占比 | 30.5% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=58.1），有序残基占 30.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015395, IPR009057, IPR017930, IPR050560, IPR001005; Pfam: PF09316, PF07988, PF00249 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CREBBP | 0.999 | 0.984 | — |
| EP300 | 0.996 | 0.828 | — |
| CEBPB | 0.980 | 0.893 | — |
| KMT2A | 0.955 | 0.856 | — |
| GATA2 | 0.945 | 0.048 | — |
| RUNX1 | 0.936 | 0.000 | — |
| SPI1 | 0.932 | 0.000 | — |
| TAL1 | 0.925 | 0.292 | — |
| MYBBP1A | 0.924 | 0.000 | — |
| GATA1 | 0.910 | 0.048 | — |

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
| 三维结构 | AlphaFold pLDDT=58.1 + PDB: 无 | pLDDT=58.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

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
1. MYB — Transcriptional activator Myb，研究基础较多，新颖性有限。
2. 蛋白大小640 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 8049 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.1），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 8049 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P10242
- Protein Atlas: https://www.proteinatlas.org/ENSG00000118513-MYB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MYB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P10242
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
