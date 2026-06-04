---
type: protein-evaluation
gene: "ATF6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ATF6 — REJECTED (研究热度过高 (PubMed strict=2739，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATF6 |
| 蛋白名称 | Cyclic AMP-dependent transcription factor ATF-6 alpha |
| 蛋白大小 | 670 aa / 74.6 kDa |
| UniProt ID | P18850 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Golgi apparatus; 额外: Nucleoli, Nucleoli fibrill; UniProt: Endoplasmic reticulum membrane; Golgi apparatus membrane; Nu |
| 蛋白大小 | 10/10 | ×1 | 10 | 670 aa / 74.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2739 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=55.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR051882, IPR004827, IPR046347; Pfam: PF00170 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Golgi apparatus; 额外: Nucleoli, Nucleoli fibrillar center, Endoplasmic reticulum, Primary cilium, Primary cilium tip, Cytosol | Supported |
| UniProt | Endoplasmic reticulum membrane; Golgi apparatus membrane; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)
- Golgi apparatus (GO:0005794)
- Golgi membrane (GO:0000139)
- membrane (GO:0016020)
- nuclear envelope (GO:0005635)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2739 |
| PubMed broad count | 3461 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The Unfolded Protein Response: An Overview.. *Biology*. PMID: 33946669
2. The unfolded protein response: controlling cell fate decisions under ER stress and beyond.. *Nature reviews. Molecular cell biology*. PMID: 22251901
3. XBP1 mRNA is induced by ATF6 and spliced by IRE1 in response to ER stress to produce a highly active transcription factor.. *Cell*. PMID: 11779464
4. GRINA alleviates hepatic ischemia‒reperfusion injury-induced apoptosis and ER-phagy by enhancing HRD1-mediated ATF6 ubiquitination.. *Journal of hepatology*. PMID: 39855351
5. ATF6 activation alters colonic lipid metabolism causing tumour-associated microbial adaptation.. *Nature metabolism*. PMID: 40890536

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 55.2 |
| 高置信度残基 (pLDDT>90) 占比 | 14.3% |
| 置信残基 (pLDDT 70-90) 占比 | 13.6% |
| 中等置信 (pLDDT 50-70) 占比 | 10.3% |
| 低置信 (pLDDT<50) 占比 | 61.8% |
| 有序区域 (pLDDT>70) 占比 | 27.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=55.2），有序残基占 27.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051882, IPR004827, IPR046347; Pfam: PF00170 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA5 | 0.999 | 0.301 | — |
| XBP1 | 0.998 | 0.574 | — |
| VAPB | 0.989 | 0.000 | — |
| DDIT3 | 0.989 | 0.000 | — |
| HSP90B1 | 0.981 | 0.000 | — |
| MBTPS2 | 0.978 | 0.000 | — |
| EIF2AK3 | 0.978 | 0.292 | — |
| ERN1 | 0.976 | 0.292 | — |
| MBTPS1 | 0.974 | 0.000 | — |
| WFS1 | 0.963 | 0.295 | — |

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
| 三维结构 | AlphaFold pLDDT=55.2 + PDB: 无 | pLDDT=55.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane; Golgi apparatus me / Nucleoplasm, Golgi apparatus; 额外: Nucleoli, Nucleo | 一致 |
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
1. ATF6 — Cyclic AMP-dependent transcription factor ATF-6 alpha，研究基础较多，新颖性有限。
2. 蛋白大小670 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2739 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=55.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2739 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P18850
- Protein Atlas: https://www.proteinatlas.org/ENSG00000118217-ATF6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATF6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P18850
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
