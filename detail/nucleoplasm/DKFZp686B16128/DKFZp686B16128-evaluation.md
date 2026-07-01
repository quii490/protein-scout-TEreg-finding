---
type: protein-evaluation
gene: "DKFZp686B16128"
date: 2026-06-28
tags: [protein-scout, nuclear-protein, evaluation, shortlisted, TE_REG_CANDIDATE]
status: shortlisted
---

## DKFZp686B16128 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | DKFZp686B16128 |
| 蛋白名称 | Uncharacterized protein DKFZp686B16128 |
| 蛋白大小 | 510 aa / 58.4 kDa |
| UniProt ID | Q68D23 |
| 评估日期 | 2026-06-28 |

### 2. 评分总览
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20.0 | nan (nan) |
| 蛋白大小 | 9/10 | ×1 | 9.0 | 510 aa |
| 新颖性 | 10/10 | ×5 | 50.0 | PubMed=0 |
| 三维结构 | 6/10 | ×3 | 18.0 | pLDDT=79.9; PDB=0 |
| 调控结构域 | 6/10 | ×2 | 12.0 | C2H2-ZF_domain; Znf_C2H2_sf; Znf_C2H2_type |
| PPI | 5/10 | ×3 | 15.0 | PPI degree=0 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.3/100** | 互证: +1 |

### 3. 分析
- nan (nan)
- PubMed strict=0 broad=0
- AF pLDDT=79.9 PDB=0
- InterPro: C2H2-ZF_domain; Znf_C2H2_sf; Znf_C2H2_type
- Pfam: zf-C2H2
- PPI degree=0 ChIP: None


### 4. 总体评价
**68.3/100** | **nucleoplasm**
TE candidate: C2H2-ZF_domain; Znf_C2H2_sf; Znf_C2H2_type


### 深度机制分析

**大分子量多锌指暗蛋白的TE靶向潜力**：DKFZp686B16128（510 aa, 58.4 kDa, UniProt Q68D23）携带3个C2H2锌指结构域分类——C2H2-ZF_domain（IPR050752）、Znf_C2H2_sf（IPR036236）和Znf_C2H2_type（IPR013087），Pfam注释为zf-C2H2（PF00096）。其UniProt注释明确指出"May be involved in transcriptional regulation"，这是本批次"暗蛋白"中与Nbla00121并列的仅有两个直接转录调控推断注解。510 aa是锌指候选中的较大者（超过DKFZp666C237的219 aa和Nbla00121的307 aa），暗示可能含有7-9个串联锌指，理论DNA识别长度为21-27 bp——远超过标准转录因子的6-12 bp识别位点，接近于ZNF91（靶向SVA的KRAB-ZNF）的锌指数目。

**锌指重复数与TE识别特异性**：ZNF91通过其31个锌指中的~16个靶向SVA-VNTR区域的CCCTCT重复序列，其中7个关键锌指的决定性DNA接触介导特异性识别。DKFZp686B16128的锌指数目（推测7-9）如果采用类似的多指串联识别模式，可产生对特定TE亚家族（如特定进化年龄段的L1PA或SVA）的高序列特异性。与Nbla00121和DKFZp666C237一样缺乏KRAB结构域，其TE沉默机制需依赖非经典通路（详见前述C2H2锌指机制分析）。PPI degree=0和PubMed=0的完全"暗物质"特征与新颖性满分（50/50）一致。

**策略性优先级**：归一化得分68.3/100中调控结构域12/30（6/10锌指）和新奇性满分50/50。考虑到蛋白大小510 aa超越了简单被动核孔扩散阈值（暗示需NLS介导核输入），以及UniProt的转录调控推断，建议在C2H2锌指暗蛋白中赋予中等优先级——低于TRIM28互作的KR-ZNF1和包含ELM2-SANT域的FLJ00335，但高于PPI=0且无转录调控注释的DKFZp666C237。


### 补充分析 (UniProt API)

**蛋白全称**: Uncharacterized protein DKFZp686B16128

**功能**: May be involved in transcriptional regulation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050752 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### 补充分析 (UniProt API)

**蛋白全称**: Uncharacterized protein DKFZp686B16128

**功能**: May be involved in transcriptional regulation

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR050752 |
| InterPro | IPR036236 |
| InterPro | IPR013087 |
| Pfam | PF00096 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---