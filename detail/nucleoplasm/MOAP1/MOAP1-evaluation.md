---
type: protein-evaluation
gene: "MOAP1"
date: 2026-06-27
tags: [protein-scout, nuclear-protein, evaluation, shortlisted]
status: shortlisted
---

## MOAP1 核蛋白评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | MOAP1 |
| 蛋白名称 | Modulator of apoptosis 1 |
| 蛋白大小 | 351 aa / 39.5 kDa |
| UniProt ID | Q96BY2 |
| 评估日期 | 2026-06-27 |

### 2. 评分总览 (新权重)
| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | x4 | 36.0 | Cell Junctions; Nucleoplasm (Approved) |
| 蛋白大小 | 9/10 | x1 | 9.0 | 351 aa |
| 新颖性 | 7/10 | x5 | 35.0 | PubMed=54 |
| 三维结构 | 7/10 | x3 | 21.0 | pLDDT=78.0; PDB=1 |
| 调控结构域 | 4/10 | x2 | 8.0 | PNMA; PNMA_C; PNMA_N |
| PPI | 5/10 | x3 | 15.0 | PPI degree=44 |
| **加权总分** | | | **124/180** | |
| **归一化总分** | | | **68.9/100** | 互证: +2 |

### 3. 分析
- Cell Junctions; Nucleoplasm (Approved)
- PubMed strict=54 broad=76
- AF pLDDT=78.0 PDB=1
- InterPro: PNMA; PNMA_C; PNMA_N
- Pfam: PNMA; PNMA_N
- PPI degree=44 ChIP: None
35269511: Revealing the Roles of MOAP1 in Diseases: A Review. | 33783314: The BAX-binding protein MOAP1 associates with LC3 and promotes closure of the ph | 34357660: Structural evidence that MOAP1 and PEG10 are derived from retrovirus/retrotransp

### 4. 总体评价
**68.9/100** | **nucleoplasm**
Nuclear protein


### 深度机制分析

**逆转座子衍生蛋白的病毒样结构域与TE同源关系**：MOAP1（Modulator of apoptosis 1, 351 aa, UniProt Q96BY2）携带PNMA（Paraneoplastic Ma antigen）结构域家族（InterPro: PNMA IPR026523, PNMA_C IPR048270, PNMA_N IPR048271; Pfam: PNMA PF14893, PNMA_N PF20846），这一结构域架构值得格外关注。PNMA家族蛋白被证实由逆转录病毒/逆转座子gag基因驯化而来，在人类中作为凋亡调控因子被"分子驯化"。PMID:34357660明确指出MOAP1和同家族蛋白PEG10均源自逆转录病毒/逆转座子Gag多蛋白的衣壳结构域——这使MOAP1成为本批次中与TE进化关系最密切的蛋白。

**病毒样衣壳组装与核内"陷阱"假说**：MOAP1的功能注释明确指出该蛋白能够形成"病毒样衣壳"（virion-like capsids），这与逆转座子Gag蛋白的古老功能直接呼应。在凋亡期间，MOAP1富集于线粒体外膜并与BAX结合，促进线粒体外膜通透化和细胞色素c释放（PMIDs:11060313, 16199525）。然而，其核质定位（Nucleoplasm Approved, 核定位特异性9/10）暗示存在非凋亡核内功能。一个富有吸引力的假说是：MOAP1在核内通过其Gag衍生衣壳域识别并包裹TE RNA/RNP颗粒，将TE逆转座中间体隔离至"不活化"状态，从而抑制TE扩增。这种"分子驯化-反向抑制"模式在果蝇中已有先例——驯化的gypsy元件Env蛋白限制同源逆转录病毒的感染。

**PPI网络中的染色质与RNA加工线索**：PPI degree=44（BioGRID/STRING），其中RASSF1（STRING score=912）和THOC1（STRING score=783）是两个关键互作节点。RASSF1的激活促进BAX构象变化和线粒体易位；THOC1是TREX mRNA出核复合物的核心组分，直接参与mRNA核质运输。此外，PNMA1（STRING score=797）和DPPA2（BioGRID score=1）支持了PNMA家族成员之间的互作网络。MOAP1-MOAP1自身互作（BioGRID score=1）与Gag衣壳蛋白的自我组装能力一致，是形成病毒样衣壳的结构基础。

**结构特性与TRE调控机制**：AlphaFold pLDDT=78.0的中等置信度结构（PDB=1存在部分晶体结构）提示PNMA域采用β-桶状折叠，与逆转录病毒衣壳蛋白的CA域结构相似。若MOAP1在核内通过衣壳化机制形成大型超分子组装体（如核内包涵体），可能物理性隔离TE转录物或逆转座中间体。然而，目前缺乏任何TE调控相关的直接实验证据，且PubMed=54的文献全部集中于凋亡和线粒体生物学。归一化得分68.9/100中核定位特异性36/40是新奇性（35/50）之外的最大贡献者。

**高优先级候选的理由与风险**：MOAP1经TE驯化起源、病毒样衣壳组装能力、核质双定位（Cell Junctions; Nucleoplasm Approved）使其成为独特的TE调控候选。主要风险为：所有已知功能均为胞质/线粒体凋亡功能，核内功能完全未知。实验验证路径：首选MOAP1 ChIP-seq检查染色质结合位点，结合RNA-IP检查其是否与TE衍生转录物互作。


### 补充分析 (UniProt API)

**蛋白全称**: Modulator of apoptosis 1

**功能**: Retrotransposon-derived protein that forms virion-like capsids (By similarity). Acts as an effector of BAX during apoptosis: enriched at outer mitochondria membrane and associates with BAX upon induction of apoptosis, facilitating BAX-dependent mitochondrial outer membrane permeabilization and apoptosis (PubMed:11060313, PubMed:16199525). Required for death receptor-dependent apoptosis (PubMed:11060313). When associated with RASSF1, promotes BAX conformational change and translocation to mitocho

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR026523 |
| InterPro | IPR048270 |
| InterPro | IPR048271 |
| Pfam | PF14893 |
| Pfam | PF20846 |

**TE 调控评估**: 该蛋白缺乏核定位证据，TE调控潜力极低。

---


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| RASSF1 | STRING | 912 |
| PNMA1 | STRING | 797 |
| THOC1 | STRING | 783 |
| MAGEH1 | BioGRID | 1 |
| DPPA2 | BioGRID | 1 |
| CCDC85B | BioGRID | 1 |
| MOAP1 | BioGRID | 1 |
| BAX | BioGRID | 1 |